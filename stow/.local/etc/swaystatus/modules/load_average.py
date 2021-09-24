from swaystatus import BaseElement


class Element(BaseElement):
    source = "/proc/loadavg"

    def on_update(self, output):
        loadavg = " ".join(open(self.source).read().split()[:-1])
        output.append(self.create_block(f"load {loadavg}"))
