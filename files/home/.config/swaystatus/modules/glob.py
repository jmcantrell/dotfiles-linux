from glob import iglob
from pathlib import Path
from swaystatus import BaseElement


class Element(BaseElement):
    name = "glob"

    def __init__(self, *args, **kwargs):
        self._kwargs = {}
        self._pattern = kwargs.pop("pattern")
        if "**" in self._pattern:
            self._kwargs["recursive"] = True
        self._kwargs["root_dir"] = kwargs.pop("root_dir")
        super().__init__(*args, **kwargs)

    def on_update(self, output):
        kwargs = {}
        for item in iglob(self._pattern, **self._kwargs):
            kwargs["instance"] = item
            output.append(self.create_block(item, **kwargs))
