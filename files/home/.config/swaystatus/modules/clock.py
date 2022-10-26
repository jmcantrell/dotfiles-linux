import time
from swaystatus.element import BaseElement


class Element(BaseElement):
    def __init__(self, *args, full_text=None, short_text=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._full_text = full_text or "%c"
        self._short_text = short_text or "%r"

    def on_update(self, output):
        full_text = time.strftime(self._full_text)
        short_text = time.strftime(self._short_text)
        output.append(self.create_block(full_text, short_text=short_text))
