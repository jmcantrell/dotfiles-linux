import subprocess
from swaystatus import BaseElement
from .util import capture_stdout
from .colors import color_off


def stereo_volume(sink):
    stdout = capture_stdout(["pactl", "get-sink-volume", sink])
    tokens = [s.strip() for s in stdout.split(" / ")]
    return [int(s.rstrip("%")) for s in tokens if s.endswith("%")]


def is_muted(sink):
    stdout = capture_stdout(["pactl", "get-sink-mute", sink])
    return stdout.split()[1] == "yes"


class Element(BaseElement):
    def __init__(self, *args, **kwargs):
        self._sink = kwargs.pop("sink", "@DEFAULT_SINK@")
        self._format = kwargs.pop("format", "audio {}")
        self._volume_format = kwargs.pop("volume_format", "{}%")
        super().__init__(*args, **kwargs)

    @property
    def _volume_text(self):
        volumes = stereo_volume(self._sink)
        if len(set(volumes)) == 1:
            return self._volume_format.format(volumes[0])
        else:
            return " / ".join([self._volume_format.format(v) for v in volumes])

    @property
    def _is_muted(self):
        return is_muted(self._sink)

    def on_update(self, output):
        kwargs = {}

        try:
            if self._is_muted:
                kwargs["color"] = color_off
            full_text = self._format.format(self._volume_text)
        except subprocess.CalledProcessError:
            return

        output.append(self.create_block(full_text, **kwargs))
