from pathlib import Path
from swaystatus import BaseElement

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


def sample():
    return proc_stat_cpu_columns("user", "system", "idle", "iowait")


class Element(BaseElement):
    def __init__(self, *args, **kwargs):
        self._format = kwargs.pop("format", "cpu {:.1f}%")
        self._previous_sample = sample()
        super().__init__(*args, **kwargs)

    def on_update(self, output):
        current_sample = sample()

        user, system, idle, iowait = values = [
            b - a for a, b in zip(self._previous_sample, current_sample)
        ]

        total = sum(values)
        active = total - idle
        percent = active * 100 / total

        self._previous_sample = current_sample

        full_text = self._format.format(percent)

        output.append(self.create_block(full_text))
