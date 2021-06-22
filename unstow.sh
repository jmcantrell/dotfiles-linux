#!/usr/bin/env bash

stow ${VERBOSE:+--verbose} --no-folding -d . -t ~ -D stow
