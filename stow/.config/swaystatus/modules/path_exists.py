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
        options = {}

        if not self._path.exists():
            options["color"] = color_off

        full_text = self._label
        instance = str(self._path)

        output.append(
            self.create_block(
                full_text,
                instance=instance,
                **options,
            )
        )
