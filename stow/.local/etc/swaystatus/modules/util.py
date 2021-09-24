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


def capture_stdout(command):
    cp = subprocess.run(command, capture_output=True, text=True)
    cp.check_returncode()
    return cp.stdout


def capture_stdout_lines(command):
    return capture_stdout(command).strip().split(os.linesep)
