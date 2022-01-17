from swaystatus import BaseElement


class Element(BaseElement):
    def on_update(self, output):
        loadavg = " ".join(open("/proc/loadavg").read().split()[:-1])
        output.append(self.create_block(f"load {loadavg}"))
