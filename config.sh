#!/usr/bin/env bash

set -euo pipefail

sudo gpasswd -a "$USER" video

sudo chsh -s /bin/zsh "$USER"
