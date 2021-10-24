import time
from swaystatus import BaseElement


class Element(BaseElement):
    def __init__(self, *args, **kwargs):
        self._format = kwargs.pop("format", "%c")
        self._format_short = kwargs.pop("format_short", "%r")
        super().__init__(*args, **kwargs)

    def on_update(self, output):
        output.append(
            self.create_block(
                time.strftime(self._format),
                short_text=time.strftime(self._format_short),
            )
        )
