#!/usr/bin/env sh

set -e

stow ${VERBOSE:+--verbose} --no-folding -d . -t ~ -D stow
