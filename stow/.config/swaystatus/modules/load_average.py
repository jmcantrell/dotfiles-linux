from pathlib import Path
from swaystatus import BaseElement


source = Path("/proc/loadavg")


def loadavg():
    with source.open() as f:
        return " ".join(f.read().split()[:-1])


class Element(BaseElement):
    def on_update(self, output):
        full_text = f"load {loadavg()}"
        output.append(self.create_block(full_text))
