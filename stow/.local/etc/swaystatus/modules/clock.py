import time
from swaystatus import BaseElement


class Element(BaseElement):
    def __init__(self, format_full="%c", format_short="%r"):
        super().__init__()
        self.format_full = format_full
        self.format_short = format_short

    def on_update(self, output):
        output.append(
            self.create_block(
                time.strftime(self.format_full),
                short_text=time.strftime(self.format_short),
            )
        )
