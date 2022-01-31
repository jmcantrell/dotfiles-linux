from subprocess import CalledProcessError
from swaystatus import BaseElement
from .util import run_quietly
from .colors import color_off


class Element(BaseElement):
    def __init__(self, *args, **kwargs):
        self._unit = kwargs.pop("unit")
        self._user = kwargs.pop("user", False)
        self._label = kwargs.pop("label", self._unit)
        super().__init__(*args, **kwargs)

    def _systemctl(self, *args):
        command = ["systemctl"]
        if self._user:
            command.append("--user")
        command.extend(args)
        return run_quietly(command)

    def _is_active(self):
        try:
            self._systemctl("is-active", self._unit)
            return True
        except CalledProcessError:
            return False

    def on_update(self, output):
        options = {}
        if not self._is_active():
            options["color"] = color_off

        output.append(
            self.create_block(
                self._label,
                instance=str(self._unit),
                **options,
            )
        )

    def on_click_1(self, _):
        self._systemctl("stop" if self._is_active() else "start", self._unit)
