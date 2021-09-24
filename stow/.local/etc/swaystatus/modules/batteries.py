from pathlib import Path
from swaystatus import BaseElement


class Element(BaseElement):
    def __init__(self):
        super().__init__()
        self.batteries = list(Path("/sys/class/power_supply").glob("BAT*"))

    def on_update(self, output):
        for battery in self.batteries:
            battery_name = battery.name.lower()
            battery_status = open(battery / "status").read().strip().lower()
            battery_capacity = open(battery / "capacity").read().strip()
            full_text = f"{battery_name} {battery_capacity}% {battery_status}"
            output.append(self.create_block(full_text, instance=battery_name))
