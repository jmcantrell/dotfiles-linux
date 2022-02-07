import subprocess
from swaystatus import BaseElement
from .util import capture_stdout


def get_status():
    return capture_stdout(["playerctl", "status"]).strip().lower()


def get_metadata(key):
    return capture_stdout(["playerctl", "metadata", key]).strip()


class Element(BaseElement):
    def on_update(self, output):
        try:
            status = get_status()
            title = get_metadata("title")
        except subprocess.CalledProcessError:
            return

        name = title

        try:
            artist = get_metadata("artist").strip()
            if artist:
                name = f"{artist} - {title}"
        except subprocess.CalledProcessError:
            pass

        full_text = f"{status}: {name}"
        short_text = f"{status} media"

        output.append(
            self.create_block(
                full_text,
                short_text=short_text,
                markup="pango",
            )
        )
