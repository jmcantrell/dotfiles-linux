#!/usr/bin/env bash

set -euo pipefail

stow --no-folding -d . -t ~ -R stow
