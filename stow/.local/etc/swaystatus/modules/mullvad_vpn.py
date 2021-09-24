from . import path_exists


class Element(path_exists.Element):
    def __init__(self):
        super().__init__(
            path="/proc/sys/net/ipv4/conf/wg-mullvad",
            label="vpn",
        )
