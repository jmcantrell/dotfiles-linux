import subprocess, html
from swaystatus import BaseElement
from .util import capture_stdout


def get_status():
    return capture_stdout(["playerctl", "status"]).strip().lower()


def get_metadata(key):
    return capture_stdout(["playerctl", "metadata", key]).strip()


class Element(BaseElement):
    def __init__(self, *args, **kwargs):
        self._format = kwargs.pop("format", "{status} {name}")
        self._format_short = kwargs.pop("format_short", "{status}")
        super().__init__(*args, **kwargs)

    def on_update(self, output):
        try:
            status = get_status()
            title = html.escape(get_metadata("title"))
        except subprocess.CalledProcessError:
            return

        name = title

        try:
            artist = html.escape(get_metadata("artist").strip())
            if artist:
                name = f'"{title}" by <u>{artist}</u>'
        except subprocess.CalledProcessError:
            pass

        format_kwargs = {"name": name, "status": status}
        full_text = self._format.format(**format_kwargs)
        short_text = self._format_short.format(**format_kwargs)

        output.append(
            self.create_block(
                full_text,
                short_text=short_text,
                markup="pango",
            )
        )
