from pathlib import Path
from swaystatus import BaseElement


class Element(BaseElement):
    _source = Path("/sys/class/power_supply")

    def on_update(self, output):
        for battery in self._source.glob("BAT*"):
            battery_name = battery.name.lower()
            battery_status = open(battery / "status").read().strip().lower()
            battery_capacity = open(battery / "capacity").read().strip()
            full_text = f"{battery_name} {battery_capacity}% {battery_status}"
            output.append(self.create_block(full_text, instance=battery_name))
