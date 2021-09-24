from pathlib import Path
from swaystatus import BaseElement


class Element(BaseElement):
    source = Path("/sys/class/net")

    def on_update(self, output):
        for interface_path in self.source.glob("*"):
            if open(interface_path / "operstate").read().strip() == "up":
                name = interface_path.name
                output.append(self.create_block(f"{name}", instance=name))
