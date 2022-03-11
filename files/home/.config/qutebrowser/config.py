import os

config.load_autoconfig()


def get_env(name, default):
    return os.environ.get(name, default)


def get_env_bool(name, default=None):
    value = get_env(name, default)
    return value if value is None else bool(int(value))


def convert_bool(value, if_truthy, if_falsy, if_none=None):
    if value is None:
        return if_none
    elif value:
        return if_truthy
    else:
        return if_falsy


def set_dark(maybe_enabled):
    if maybe_enabled is None:
        return

    config.set("colors.webpage.darkmode.enabled", maybe_enabled)
    config.set(
        "colors.webpage.preferred_color_scheme",
        convert_bool(maybe_enabled, "dark", "light"),
    )

    if not maybe_enabled:
        config.set("colors.webpage.bg", None)


set_dark(get_env_bool("QUTE_OVERRIDE_DARK"))
