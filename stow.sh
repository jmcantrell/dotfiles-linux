#!/usr/bin/env sh

stow ${VERBOSE:+--verbose} --no-folding -d . -t ~ -R stow
