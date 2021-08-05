#!/usr/bin/env bash

set -euo pipefail

sudo ufw enable
sudo ufw default deny
sudo ufw allow ssh
sudo ufw allow mdns
sudo ufw allow llmnr

sudo gpasswd -a "$USER" video

sudo chsh -s /bin/zsh "$USER"

updatedb
