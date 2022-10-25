import subprocess, html
from swaystatus import BaseElement
from .util import capture_stdout


def get_status():
    return capture_stdout(["playerctl", "status"]).strip().lower()


def get_metadata(key):
    return capture_stdout(["playerctl", "metadata", key]).strip()


class Element(BaseElement):
    def __init__(self, *args, full_text=None, short_text=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._full_text = full_text or "{status} {name}"
        self._short_text = short_text or "{status}"

    def on_update(self, output):
        try:
            status = get_status()
            title = get_metadata("title")
            artist = get_metadata("artist")
        except subprocess.CalledProcessError:
            return

        name = html.escape(title)
        if artist:
            name = f'"{title}" by <u>{html.escape(artist)}</u>'

        kwargs = {"name": name, "status": status}
        full_text = self._full_text.format(**kwargs)
        short_text = self._short_text.format(**kwargs)

        output.append(
            self.create_block(
                full_text,
                short_text=short_text,
                markup="pango",
            )
        )
