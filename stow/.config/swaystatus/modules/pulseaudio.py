import subprocess
from swaystatus import BaseElement
from .util import capture_stdout
from .colors import color_off


class Element(BaseElement):
    def __init__(self, *args, **kwargs):
        self._sink = kwargs.pop("sink", "@DEFAULT_SINK@")
        super().__init__(*args, **kwargs)

    @property
    def _stereo_volume(self):
        stdout = capture_stdout(["pactl", "get-sink-volume", self._sink])
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
        stdout = capture_stdout(["pactl", "get-sink-mute", self._sink])
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
