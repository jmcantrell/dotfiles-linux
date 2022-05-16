from pathlib import Path
from swaystatus import BaseElement
from .colors import color_off


class Element(BaseElement):
    def __init__(self, *args, **kwargs):
        path = kwargs.pop("path", "/")
        self._path = Path(path).expanduser()
        self._label = kwargs.pop("label", path)
        super().__init__(*args, **kwargs)

    def on_update(self, output):
        kwargs = {}

        if not self._path.exists():
            kwargs["color"] = color_off

        kwargs["instance"] = str(self._path)

        output.append(self.create_block(self._label, **kwargs))
