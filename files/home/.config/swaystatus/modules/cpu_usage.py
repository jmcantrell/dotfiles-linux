from pathlib import Path
from swaystatus.element import BaseElement

source = Path("/proc/stat")

columns = [
    "user",
    "nice",
    "system",
    "idle",
    "iowait",
    "irq",
    "softirq",
    "steal",
    "guest",
    "guest_nice",
]

column_index = {column: index for index, column in enumerate(columns)}


def proc_stat_cpu():
    with source.open() as f:
        return f.readline().strip().split()[1:]


def proc_stat_cpu_columns(*columns):
    values = proc_stat_cpu()
    return [int(values[column_index[column]]) for column in columns]


def proc_stat_sample():
    return proc_stat_cpu_columns("user", "system", "idle", "iowait")


class Element(BaseElement):
    def __init__(self, *args, full_text=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._full_text = full_text or "cpu {:.1f}%"
        self._previous_sample = proc_stat_sample()

    def on_update(self, output):
        sample = proc_stat_sample()
        values = [b - a for a, b in zip(self._previous_sample, sample)]
        total = sum(values)

        if total == 0:
            percent = 0
        else:
            active = total - values[2]  # idle
            percent = active * 100 / total

        self._previous_sample = sample

        full_text = self._full_text.format(percent)
        output.append(self.create_block(full_text))
