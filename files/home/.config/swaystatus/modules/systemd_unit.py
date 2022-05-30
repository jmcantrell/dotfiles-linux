from subprocess import CalledProcessError
from swaystatus import BaseElement
from .util import run_quietly
from .colors import color_off


def systemctl(*args, user=False):
    command = ["systemctl"]
    if user:
        command.append("--user")
    command.extend(args)
    return run_quietly(command)


def is_active(unit, **kwargs):
    try:
        systemctl("is-active", unit, **kwargs)
        return True
    except CalledProcessError:
        return False


class Element(BaseElement):
    name = "systemd_unit"

    def __init__(self, *args, **kwargs):
        self._unit = kwargs.pop("unit")
        self._user = kwargs.pop("user", False)
        self._label = kwargs.pop("label", self._unit)
        super().__init__(*args, **kwargs)

    def _systemctl(self, *args):
        return systemctl(*args, self._unit, user=self._user)

    @property
    def _is_active(self):
        return is_active(self._unit, user=self._user)

    def on_update(self, output):
        kwargs = {}

        if not is_active(self._unit, user=self._user):
            kwargs["color"] = color_off

        kwargs["instance"] = str(self._unit)

        output.append(self.create_block(self._label, **kwargs))

    def on_click_1(self, _):
        self._systemctl("stop" if self._is_active else "start")
