#!/usr/bin/env bash

stow ${VERBOSE:+--verbose} --no-folding -d . -t ~ -R stow
