import subprocess
from swaystatus import BaseElement
from .util import capture_stdout
from .colors import color_off


def get_stereo_volume(sink):
    stdout = capture_stdout(["pactl", "get-sink-volume", sink])
    return [
        int(s.strip().rstrip("%"))
        for s in stdout.split(" / ")
        if s.endswith("%")
    ]


def get_muted(sink):
    stdout = capture_stdout(["pactl", "get-sink-mute", sink])
    return stdout.split()[1] == "yes"


class Element(BaseElement):
    def __init__(self, *args, **kwargs):
        self._sink = kwargs.pop("sink", "@DEFAULT_SINK@")
        super().__init__(*args, **kwargs)

    @property
    def _volume_text(self):
        volumes = get_stereo_volume(self._sink)
        volume_format = "{}%"
        if len(set(volumes)) == 1:
            return volume_format.format(volumes[0])
        else:
            return " / ".join([volume_format.format(v) for v in volumes])

    def on_update(self, output):
        try:
            kwargs = {}

            if get_muted(self._sink):
                kwargs["color"] = color_off

            full_text = f"audio {self._volume_text}"

            output.append(self.create_block(full_text, **kwargs))
        except subprocess.CalledProcessError:
            return
