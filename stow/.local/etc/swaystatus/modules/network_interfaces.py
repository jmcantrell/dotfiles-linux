from pathlib import Path
from swaystatus import BaseElement


class Element(BaseElement):
    _source = Path("/sys/class/net")

    def on_update(self, output):
        for interface_path in self._source.glob("*"):
            if open(interface_path / "operstate").read().strip() == "up":
                name = interface_path.name
                output.append(self.create_block(f"{name}", instance=name))
