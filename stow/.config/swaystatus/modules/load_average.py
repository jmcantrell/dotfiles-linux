from pathlib import Path
from swaystatus import BaseElement


class Element(BaseElement):
    _source = Path("/proc/loadavg")

    @property
    def _loadavg(self):
        with self._source.open() as f:
            return " ".join(f.read().split()[:-1])

    def on_update(self, output):
        full_text = f"load {self._loadavg}"
        output.append(self.create_block(full_text))
