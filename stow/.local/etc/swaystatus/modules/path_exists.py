from pathlib import Path
from swaystatus import BaseElement


class Element(BaseElement):
    def __init__(self, path=None, label=None):
        super().__init__()
        self.path = Path(path).expanduser()
        self.label = label or path

    def on_update(self, output):
        if self.path.exists():
            output.append(
                self.create_block(
                    self.label,
                    instance=str(self.path),
                )
            )
