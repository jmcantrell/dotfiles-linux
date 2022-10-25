from pathlib import Path
from swaystatus import BaseElement

source = Path("/sys/class/power_supply")


def battery_attr(battery, attr):
    with (battery / attr).open() as f:
        return f.read().strip()


class Element(BaseElement):
    def __init__(self, *args, full_text=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._full_text = full_text or "{name} {capacity}% {status}"

    def on_update(self, output):
        for battery in source.glob("BAT*"):
            name = battery.name.lower()
            kwargs = {
                "name": name,
                "capacity": battery_attr(battery, "capacity"),
                "status": battery_attr(battery, "status").lower(),
            }
            full_text = self._full_text.format(**kwargs)
            output.append(self.create_block(full_text, instance=name))
