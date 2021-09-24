from swaystatus import BaseElement
from .util import bytes2human


class Element(BaseElement):
    source = "/proc/meminfo"

    def __init__(self, key="MemAvailable"):
        super().__init__()
        self.line_number = self._find_line_number(key)

    def _find_line_number(self, key):
        line_number = 0

        for line in open(self.source).readlines():
            if line.startswith(key + ":"):
                return line_number
            line_number += 1

        raise KeyError(f"Key '{key}' not found in {self.source}")

    def on_update(self, output):
        line = open(self.source).readlines()[self.line_number]
        free = int(line.split(":")[1].strip().split()[0]) * 1024
        output.append(self.create_block(f"mem {bytes2human(free)}"))
