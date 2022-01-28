from pathlib import Path
from swaystatus import BaseElement


class Element(BaseElement):
    _source = Path("/sys/class/power_supply")

    def _battery_status(self, battery):
        with (battery / "status").open() as f:
            return f.read().strip().lower()

    def _battery_capacity(self, battery):
        with (battery / "capacity").open() as f:
            return f.read().strip()

    def on_update(self, output):
        for battery in self._source.glob("BAT*"):
            name = battery.name.lower()
            status = self._battery_status(battery)
            capacity = self._battery_capacity(battery)
            full_text = f"{name} {capacity}% {status}"
            output.append(self.create_block(full_text, instance=name))
