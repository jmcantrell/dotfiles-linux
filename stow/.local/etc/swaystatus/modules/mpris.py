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
            artist = self._metadata("artist")
            title = self._metadata("title")
        except subprocess.CalledProcessError:
            return

        full_text = title
        full_text = f"{full_text} - {artist}" if artist else full_text
        full_text = f"{status}: {full_text}"

        output.append(
            self.create_block(
                full_text,
                short_text=f"{status} media",
                markup="pango",
            )
        )
