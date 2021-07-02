#!/usr/bin/env bash

set -euo pipefail

stow ${VERBOSE:+--verbose} --no-folding -d . -t ~ -R stow
