#!/usr/bin/env bash

set -euo pipefail

sudo ufw enable
sudo ufw default deny
sudo ufw allow ssh
sudo ufw allow mdns
sudo ufw allow llmnr

# Needed to change screen brightness.
sudo gpasswd -a "$USER" video

sudo gpasswd -a "$USER" locate
updatedb

sudo chsh -s /bin/zsh "$USER"
