#!/usr/bin/env bash

set -e

# ca certs can be in different places, so link to a common place
mkdir -p ~/.local/etc/ssl/certs
ln -sfv /etc/ssl/certs/ca-certificates.crt ~/.local/etc/ssl/certs/ca-certificates.crt

# change shell to zsh
[[ ${SHELL##*/} = zsh ]] || chsh -s /bin/zsh
