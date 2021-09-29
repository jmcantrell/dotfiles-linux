from pathlib import Path
from swaystatus import BaseElement
from .colors import color_off


class Element(BaseElement):
    def __init__(self, path=None, label=None):
        super().__init__()
        self.path = Path(path).expanduser()
        self.label = label or path

    def on_update(self, output):
        options = {}
        if not self.path.exists():
            options["color"] = color_off

        output.append(
            self.create_block(
                self.label,
                instance=str(self.path),
                **options,
            )
        )
