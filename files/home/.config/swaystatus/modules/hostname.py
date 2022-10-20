from pathlib import Path
from swaystatus import BaseElement

source = Path("/etc/hostname")


class Element(BaseElement):
    def __init__(self, *args, **kwargs):
        self._format = kwargs.pop("format", "{}")
        self._watch = kwargs.pop("watch", False)
        super().__init__(*args, **kwargs)
        self._last_update = 0
        self._cached_hostname = None

    @property
    def _was_updated(self):
        return source.stat().st_mtime > self._last_update

    @property
    def _hostname(self):
        if not self._cached_hostname or (self._watch and self._was_updated):
            self._cached_hostname = source.read_text().strip()
        return self._cached_hostname

    def on_update(self, output):
        full_text = self._format.format(self._hostname)
        output.append(self.create_block(full_text))
