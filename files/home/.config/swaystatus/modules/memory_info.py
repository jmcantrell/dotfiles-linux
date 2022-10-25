from pathlib import Path
from swaystatus import BaseElement
from .util import bytes_to_human, get_file_line

source = Path("/proc/meminfo")


def find_line_number(key):
    line_number = 1

    with source.open() as f:
        for line in f:
            if line.startswith(key + ":"):
                return line_number
            line_number += 1

    raise KeyError(f"Key '{key}' not found in {source}")


def get_line_kbytes(line_number):
    line = get_file_line(source, line_number)
    return int(line.split(":", maxsplit=1)[1].strip().split(maxsplit=1)[0])


class Element(BaseElement):
    def __init__(self, *args, key=None, full_text=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._key = key or "MemAvailable"
        self._line_number = find_line_number(self._key)
        self._full_text = full_text or "mem {}"

    def on_update(self, output):
        memory_bytes = get_line_kbytes(self._line_number) * 1024
        full_text = self._full_text.format(bytes_to_human(memory_bytes))
        output.append(self.create_block(full_text))
