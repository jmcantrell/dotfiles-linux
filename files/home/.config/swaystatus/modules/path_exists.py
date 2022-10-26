from pathlib import Path
from swaystatus.element import BaseElement
from .colors import color_off


class Element(BaseElement):
    def __init__(self, *args, path=None, full_text=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._path = Path(path)
        self._full_text = full_text or "{}"

    def on_update(self, output):
        kwargs = {}
        if not self._path.expanduser().exists():
            kwargs["color"] = color_off

        full_text = self._full_text.format(str(self._path))
        output.append(self.create_block(full_text, **kwargs))
