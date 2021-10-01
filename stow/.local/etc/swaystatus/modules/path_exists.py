from pathlib import Path
from swaystatus import BaseElement
from .colors import color_off


class Element(BaseElement):
    def __init__(self, *args, **kwargs):
        path = kwargs.pop("path", "/")
        self.path = Path(path).expanduser()
        self.label = kwargs.pop("label", path)
        super().__init__(*args, **kwargs)

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
