import os, logging

logger = logging.getLogger("config")


def boolenv(s):
    return bool(int(s))


def override(name, key, convert=str):
    var = f"QUTEBROWSER_{name}"
    if var in os.environ:
        value = convert(os.environ[var])
        logger.info(f"Overriding {key} with {value}")
        config.set(key, value)


config.load_autoconfig()

override("DARKMODE", "colors.webpage.darkmode.enabled", convert=boolenv)
