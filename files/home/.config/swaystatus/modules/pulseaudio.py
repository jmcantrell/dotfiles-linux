import subprocess
from swaystatus.element import BaseElement
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
    def __init__(self, *args, sink=None, full_text=None, volume_text=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._sink = sink or "@DEFAULT_SINK@"
        self._full_text = full_text or "audio {}"
        self._volume_text = volume_text or "{}%"

    def on_update(self, output):
        try:
            muted = is_muted(self._sink)
            volumes = stereo_volume(self._sink)
        except subprocess.CalledProcessError:
            return

        kwargs = {}
        if muted:
            kwargs["color"] = color_off

        if len(set(volumes)) == 1:
            volume_text = self._volume_text.format(volumes[0])
        else:
            volume_text = " / ".join([self._volume_text.format(v) for v in volumes])

        full_text = self._full_text.format(volume_text)
        output.append(self.create_block(full_text, **kwargs))
