from pathlib import Path
from swaystatus import BaseElement

source = Path("/sys/class/power_supply")


def battery_attr(battery, attr):
    with (battery / attr).open() as f:
        return f.read().strip()


class Element(BaseElement):
    name = "batteries"

    def __init__(self, *args, **kwargs):
        self._format = kwargs.pop("format", "{name} {capacity}% {status}")
        super().__init__(*args, **kwargs)

    def on_update(self, output):
        for battery in source.glob("BAT*"):
            name = battery.name.lower()
            format_kwargs = {
                "name": name,
                "capacity": battery_attr(battery, "capacity"),
                "status": battery_attr(battery, "status").lower(),
            }
            full_text = self._format.format(**format_kwargs)
            output.append(self.create_block(full_text, instance=name))
