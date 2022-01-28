from pathlib import Path
from swaystatus import BaseElement


class Element(BaseElement):
    _source = Path("/sys/class/net")

    def _operstate(self, interface):
        with (interface / "operstate").open() as f:
            return f.read().strip()

    def on_update(self, output):
        for interface in self._source.glob("*"):
            if self._operstate(interface) == "up":
                name = interface.name
                output.append(self.create_block(f"{name}", instance=name))
