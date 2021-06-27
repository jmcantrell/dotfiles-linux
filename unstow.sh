#!/usr/bin/env sh

stow ${VERBOSE:+--verbose} --no-folding -d . -t ~ -D stow
