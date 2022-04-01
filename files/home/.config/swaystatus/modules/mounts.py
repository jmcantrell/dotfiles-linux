import os
from pathlib import Path
from swaystatus import BaseElement
from .util import bytes_to_human

source = Path("/proc/mounts")

ignore_types = {
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


def mounted_paths():
    with source.open() as f:
        lines = f.readlines()

    paths = []
    seen_devices = set()

    for line in lines:
        device, mount, type = line.strip().split()[0:3]
        if type not in ignore_types and device not in seen_devices:
            seen_devices.add(device)
            paths.append(Path(mount))

    return paths


def path_free_bytes(path):
    stat = os.statvfs(path)
    return stat.f_frsize * stat.f_bfree


class Element(BaseElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_update(self, output):
        for path in mounted_paths():
            instance = str(path)
            label = path.name or "root"
            try:
                free_bytes = path_free_bytes(path)
                free = bytes_to_human(free_bytes)
                full_text = f"{label} {free}"
            except PermissionError:
                full_text = label
            output.append(self.create_block(full_text, instance=instance))
