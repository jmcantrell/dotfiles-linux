#!/usr/bin/env bash

set -eu

# Needed to change screen brightness.
sudo gpasswd -a "$USER" video

sudo gpasswd -a "$USER" locate
sudo updatedb

sudo chsh -s /bin/zsh "$USER"
