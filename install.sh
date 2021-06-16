#!/usr/bin/env bash

set -e

rsync -av ./copy/ "$HOME"

# If the user directories don't already exist, xdg-user-dirs-update will just
# change the setting in the config file to $HOME, so this will create them.
grep "^XDG_" ~/.config/user-dirs.dirs | cut -d= -f1 | while read -r name; do
    mkdir -p "$(xdg-user-dir "$name")"
done
