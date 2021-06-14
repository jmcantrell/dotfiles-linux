#!/usr/bin/env bash

set -e

vmsdir=$HOME/.virtualbox
mkdir -p "$vmsdir"
# disable btrfs copy-on-write for vms folder
fstype=$(mount | grep " $(dirname "$HOME") " | cut -d' ' -f5)
[[ "$fstype" = btrfs ]] && chattr +C "$vmsdir"

vboxmanage setproperty machinefolder "$vmsdir"

# ca certs can be in different places, so link to a common place
mkdir -p ~/.local/etc/ssl/certs
ln -sfv /etc/ssl/certs/ca-certificates.crt ~/.local/etc/ssl/certs/ca-certificates.crt

# friendlier access to udiskie removable disks
ln -svfT "/run/media/$USER" "$HOME/.local/media"

rsync -av ./copy/ "$HOME"

grep "^XDG_" ~/.config/user-dirs.dirs | cut -d= -f1 | while read -r name; do
    mkdir -p "$(xdg-user-dir "$name")"
done
