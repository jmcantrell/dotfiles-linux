import os
from pathlib import Path
from swaystatus import BaseElement
from .util import bytes2human


class Element(BaseElement):
    def __init__(self, *args, **kwargs):
        path = Path(kwargs.pop("path", "/"))
        self.path = path.expanduser()
        self.label = kwargs.pop("label", str(path))
        super().__init__(*args, **kwargs)

    def on_update(self, output):
        stat = os.statvfs(self.path)
        free = stat.f_frsize * stat.f_bfree
        full_text = f"{self.label} {bytes2human(free)}"
        output.append(self.create_block(full_text, instance=str(self.path)))
