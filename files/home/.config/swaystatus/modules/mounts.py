import os
from pathlib import Path
from swaystatus import BaseElement
from .util import bytes_to_human

source = Path("/proc/mounts")

ignore_vfstypes = {
    "autofs",
    "binfmt_misc",
    "bpf",
    "cgroup",
    "cgroup2",
    "configfs",
    "debugfs",
    "devpts",
    "devtmpfs",
    "fuse.gvfsd-fuse",
    "fuse.portal",
    "fusectl",
    "hugetlbfs",
    "mqueue",
    "nsfs",
    "proc",
    "pstore",
    "ramfs",
    "securityfs",
    "sysfs",
    "tmpfs",
    "tracefs",
}

nosize_vfstypes = {"iso9660"}


def mounted_paths():
    with source.open() as f:
        lines = f.readlines()

    paths = []
    seen_devices = set()

    for line in lines:
        device, mount, vfstype = line.strip().split()[0:3]
        if vfstype not in ignore_vfstypes and device not in seen_devices:
            seen_devices.add(device)
            paths.append([Path(mount), vfstype])

    paths.sort()

    return paths


def path_free_bytes(path):
    stat = os.statvfs(path)
    return stat.f_frsize * stat.f_bfree


class Element(BaseElement):
    name = "mounts"

    def __init__(self, *args, **kwargs):
        self._format = kwargs.pop("format", "{label} {free}")
        super().__init__(*args, **kwargs)

    def on_update(self, output):
        for path, vfstype in mounted_paths():
            instance = str(path)
            label = path.name or "root"
            format_kwargs = {"label": label, "free": ""}
            if vfstype not in nosize_vfstypes:
                try:
                    free_bytes = path_free_bytes(path)
                    format_kwargs["free"] = bytes_to_human(free_bytes)
                except PermissionError:
                    pass
            full_text = self._format.format(**format_kwargs).strip()
            output.append(self.create_block(full_text, instance=instance))
