#!/usr/bin/env bash

set -e

export PATH=$PWD/bin:$PATH

stow --no-folding -d . -t ~ -R stow
