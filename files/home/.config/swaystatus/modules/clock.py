import time
from swaystatus import BaseElement


class Element(BaseElement):

    def __init__(self, *args, **kwargs):
        self._format = kwargs.pop("format", "%c")
        self._format_short = kwargs.pop("format_short", "%r")
        super().__init__(*args, **kwargs)

    def on_update(self, output):
        full_text = time.strftime(self._format)
        short_text = time.strftime(self._format_short)
        output.append(self.create_block(full_text, short_text=short_text))
