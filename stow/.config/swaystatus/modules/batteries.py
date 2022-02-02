from pathlib import Path
from swaystatus import BaseElement


class Element(BaseElement):
    _source = Path("/sys/class/power_supply")

    def _battery_attr(self, battery, attr):
        with (battery / attr).open() as f:
            return f.read().strip()

    def on_update(self, output):
        for battery in self._source.glob("BAT*"):
            name = battery.name.lower()
            status = self._battery_attr(battery, "status").lower()
            capacity = self._battery_attr(battery, "capacity")
            full_text = f"{name} {capacity}% {status}"
            output.append(self.create_block(full_text, instance=name))
