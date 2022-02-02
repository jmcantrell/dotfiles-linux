from pathlib import Path
from swaystatus import BaseElement
from .util import bytes_to_human, get_file_line


class Element(BaseElement):
    _source = Path("/proc/meminfo")

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

    @property
    def _memory_kbytes(self):
        return int(
            get_file_line(self._source, self._line_number)
            .split(":", maxsplit=1)[1]
            .strip()
            .split(maxsplit=1)[0]
        )

    def on_update(self, output):
        memory_bytes = self._memory_kbytes * 1024
        memory_human = bytes_to_human(memory_bytes)
        full_text = f"mem {memory_human}"
        output.append(self.create_block(full_text))
