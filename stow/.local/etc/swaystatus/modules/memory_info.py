from linecache import getline
from swaystatus import BaseElement
from .util import bytes2human


class Element(BaseElement):
    _source = "/proc/meminfo"

    def __init__(self, *args, **kwargs):
        self._line_number = self._find_line_number(
            kwargs.pop("key", "MemAvailable")
        )
        super().__init__(*args, **kwargs)

    def _find_line_number(self, key):
        line_number = 1

        for line in open(self._source):
            if line.startswith(key + ":"):
                return line_number
            line_number += 1

        raise KeyError(f"Key '{key}' not found in {self._source}")

    def on_update(self, output):
        free = (
            int(
                getline(self._source, self._line_number)
                .split(":", maxsplit=1)[1]
                .strip()
                .split(maxsplit=1)[0]
            )
            * 1024
        )
        output.append(self.create_block(f"mem {bytes2human(free)}"))
