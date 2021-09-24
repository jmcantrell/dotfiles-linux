import subprocess
from swaystatus import BaseElement
from .util import capture_stdout
from .colors import color_off


class Element(BaseElement):
    sink = "@DEFAULT_SINK@"

    @property
    def _stereo_volume(self):
        stdout = capture_stdout(["pactl", "get-sink-volume", self.sink])
        return [
            int(s.strip().rstrip("%"))
            for s in stdout.split(" / ")
            if s.endswith("%")
        ]

    @property
    def _volume_text(self):
        volumes = self._stereo_volume
        volume_format = "{}%"
        if len(set(volumes)) == 1:
            return volume_format.format(volumes[0])
        else:
            return " / ".join([volume_format.format(v) for v in volumes])

    @property
    def _muted(self):
        stdout = capture_stdout(["pactl", "get-sink-mute", self.sink])
        return stdout.split()[1] == "yes"

    def on_update(self, output):
        try:
            kwargs = {}
            if self._muted:
                kwargs["color"] = color_off
            output.append(
                self.create_block(f"audio {self._volume_text}", **kwargs)
            )
        except subprocess.CalledProcessError:
            return

    def _toggle_mute(self):
        subprocess.run(["pactl", "set-sink-mute", self.sink, "toggle"])

    def _set_volume(self, volume):
        subprocess.run(["pactl", "set-sink-volume", self.sink, volume])

    def _open_mixer(self):
        try:
            subprocess.run(["pavucontrol"])
        except subprocess.CompletedProcess:
            pass

    def on_click_1(self, event):
        self._toggle_mute()

    def on_click_3(self, event):
        self._open_mixer()

    def on_click_4(self, event):
        self._set_volume("+5%")

    def on_click_5(self, event):
        self._set_volume("-5%")
