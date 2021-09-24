import os
from swaystatus import BaseElement
from .util import bytes2human


class Element(BaseElement):
    def __init__(self, path="/", label=None):
        super().__init__()
        self.path = os.path.expanduser(path)
        self.label = label or path.replace(os.path.expanduser("~"), "~")

    def on_update(self, output):
        stat = os.statvfs(self.path)
        free = stat.f_frsize * stat.f_bfree
        full_text = f"{self.label} {bytes2human(free)}"
        output.append(self.create_block(full_text, instance=self.path))
