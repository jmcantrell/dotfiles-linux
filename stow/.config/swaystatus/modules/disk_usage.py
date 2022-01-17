import os
from pathlib import Path
from swaystatus import BaseElement
from .util import bytes2human


class Element(BaseElement):
    def __init__(self, *args, **kwargs):
        path = Path(kwargs.pop("path", "/"))
        self._path = path.expanduser()
        self._label = kwargs.pop("label", str(path))
        super().__init__(*args, **kwargs)

    def on_update(self, output):
        stat = os.statvfs(self._path)
        free = stat.f_frsize * stat.f_bfree
        full_text = f"{self._label} {bytes2human(free)}"
        output.append(self.create_block(full_text, instance=str(self._path)))