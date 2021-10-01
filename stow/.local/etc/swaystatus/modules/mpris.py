import subprocess
from swaystatus import BaseElement
from .util import capture_stdout


class Element(BaseElement):
    def _status(self):
        return capture_stdout(["playerctl", "status"]).strip().lower()

    def _metadata(self, key):
        return capture_stdout(["playerctl", "metadata", key]).strip()

    def on_update(self, output):
        try:
            status = self._status()
            title = self._metadata("title")
        except subprocess.CalledProcessError:
            return

        name = title

        try:
            artist = self._metadata("artist").strip()
            if artist:
                name = f"{artist} - {title}"
        except subprocess.CalledProcessError:
            pass

        output.append(
            self.create_block(
                full_text=f"{status}: {name}",
                short_text=f"{status} media",
                markup="pango",
            )
        )
