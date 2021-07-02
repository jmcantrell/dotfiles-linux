#!/usr/bin/env bash

set -euo pipefail

rsync -av ./copy/ "$HOME"

# If the user directories don't already exist, xdg-user-dirs-update will just
# change the setting in the config file to $HOME, so this will create them.
grep "^XDG_" ~/.config/user-dirs.dirs |
    awk -F= '{print $1}' | awk -F_ '{print $2}' |
    xargs -r -I{} xdg-user-dir {} | xargs -r -I{} mkdir -p "{}"
