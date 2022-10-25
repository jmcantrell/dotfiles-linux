import os, subprocess
from subprocess import DEVNULL

data_sizes_in_bytes = {}
data_size_symbols = "YZEPTGMKB"
for i, s in enumerate(reversed(data_size_symbols[:-1])):
    data_sizes_in_bytes[s] = 1 << (i + 1) * 10


def bytes_to_human(value, fmt=None):
    if value == 0:
        return "0"

    fmt = fmt or "{value:n} {symbol}"

    for symbol in data_size_symbols[:-1]:
        if value >= data_sizes_in_bytes[symbol]:
            value /= data_sizes_in_bytes[symbol]
            return fmt.format(value=round(value, 1), symbol=symbol)

    return fmt.format(value=value, symbol=data_size_symbols[-1])


def run(command, *args, **kwargs):
    cp = subprocess.run(command, *args, **kwargs)
    cp.check_returncode()
    return cp


def run_quietly(command, *args, **kwargs):
    kwargs["stdout"] = DEVNULL
    return run(command, *args, **kwargs)


def capture_stdout(command, **kwargs):
    return run(command, capture_output=True, text=True, **kwargs).stdout


def capture_stdout_lines(command, **kwargs):
    return capture_stdout(command).strip().split(os.linesep)


def get_file_line(file, line_number):
    with file.open() as f:
        for i, line in enumerate(f):
            if i + 1 == line_number:
                return line
