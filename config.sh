#!/usr/bin/env bash

set -euo pipefail

# Needed to change screen brightness.
sudo gpasswd -a "$USER" video

sudo gpasswd -a "$USER" locate
sudo updatedb

sudo chsh -s /bin/zsh "$USER"
