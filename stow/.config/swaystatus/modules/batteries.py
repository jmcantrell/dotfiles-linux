from pathlib import Path
from swaystatus import BaseElement

source = Path("/sys/class/power_supply")


def battery_attr(battery, attr):
    with (battery / attr).open() as f:
        return f.read().strip()


class Element(BaseElement):
    def on_update(self, output):
        for battery in source.glob("BAT*"):
            name = battery.name.lower()
            status = battery_attr(battery, "status").lower()
            capacity = battery_attr(battery, "capacity")
            full_text = f"{name} {capacity}% {status}"
            output.append(self.create_block(full_text, instance=name))
