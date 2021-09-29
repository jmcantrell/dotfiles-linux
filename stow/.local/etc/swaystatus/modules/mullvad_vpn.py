from . import path_exists
from .util import capture_stdout, run_safe


class Element(path_exists.Element):
    def __init__(self):
        super().__init__(
            path="/proc/sys/net/ipv4/conf/wg-mullvad",
            label="vpn",
        )

    def _is_connected(self):
        return capture_stdout(["mullvad", "status"]).split()[2] == "Connected"

    def on_click_1(self, event):
        run_safe(
            ["mullvad", "disconnect" if self._is_connected() else "connect"]
        )
