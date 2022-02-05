from pathlib import Path
from swaystatus import BaseElement

source = Path("/sys/class/net")


def operstate(interface):
    with (interface / "operstate").open() as f:
        return f.read().strip()


class Element(BaseElement):
    def on_update(self, output):
        for interface in source.glob("*"):
            if operstate(interface) == "up":
                full_text = instance = interface.name
                output.append(self.create_block(full_text, instance=instance))
