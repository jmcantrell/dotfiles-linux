import os, logging

logger = logging.getLogger("config")


def boolenv(s):
    return bool(int(s))


def override(name, key, default=None, convert=str):
    var = f"QUTEBROWSER_{name}"
    if var in os.environ:
        value = default or convert(os.environ[var])
        logger.info(f"Overriding {key} with {value}")
        config.set(key, value)


config.load_autoconfig()

override("DARKMODE", "colors.webpage.darkmode.enabled", convert=boolenv)

if not c.colors.webpage.darkmode.enabled:
    c.colors.webpage.bg = "white"
