from subprocess import CalledProcessError
from swaystatus.element import BaseElement
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
    def __init__(self, *args, unit=None, user=False, full_text=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._user = user
        self._unit = unit or (user and "session.slice") or "user.slice"
        self._full_text = full_text or self._unit

    def _systemctl(self, *args):
        return systemctl(*args, self._unit, user=self._user)

    @property
    def _is_active(self):
        return is_active(self._unit, user=self._user)

    def on_update(self, output):
        kwargs = {"instance": str(self._unit)}
        if not self._is_active:
            kwargs["color"] = color_off

        output.append(self.create_block(self._full_text, **kwargs))

    def on_click_1(self, _):
        self._systemctl("stop" if self._is_active else "start")
