import os
import subprocess

data_sizes_in_bytes = {}
data_size_symbols = "BKMGTPEZY"
for i, s in enumerate(data_size_symbols[1:]):
    data_sizes_in_bytes[s] = 1 << (i + 1) * 10


def bytes2human(value, fmt="{value:.1f} {symbol}"):
    for symbol in reversed(data_size_symbols[1:]):
        if value >= data_sizes_in_bytes[symbol]:
            value = value / data_sizes_in_bytes[symbol]
            return fmt.format(symbol=symbol, value=value)
    return fmt.format(symbol=data_size_symbols[0], value=value)


def run_safe(command, *args, **kwargs):
    cp = subprocess.run(command, *args, **kwargs)
    cp.check_returncode()
    return cp


def capture_stdout(command):
    return run_safe(command, capture_output=True, text=True).stdout


def capture_stdout_lines(command):
    return capture_stdout(command).strip().split(os.linesep)


def get_file_line(file, line_number):
    with file.open() as f:
        for i, line in enumerate(f):
            if i + 1 == line_number:
                return line
