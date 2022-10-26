from pathlib import Path
from swaystatus.element import BaseElement

source = Path("/sys/class/net")


def interface_attr(interface, attr):
    with (interface / attr).open() as f:
        return f.read().strip()


class Element(BaseElement):
    def on_update(self, output):
        for interface in source.glob("*"):
            if interface_attr(interface, "operstate") == "up":
                full_text = instance = interface.name
                output.append(self.create_block(full_text, instance=instance))
