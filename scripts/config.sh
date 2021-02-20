#!/usr/bin/env bash

set -e

# only if allowed to use sudo
if groups | grep -wq wheel; then

    # disable pc speaker
    echo "blacklist pcspkr" | sudo tee /etc/modprobe.d/pcspkr.conf

fi

# ca certs can be in different places, so link to a common place
mkdir -p ~/.local/etc/ssl/certs
ln -sfv /etc/ssl/certs/ca-certificates.crt ~/.local/etc/ssl/certs/ca-certificates.crt

# change shell to zsh
[[ ${SHELL##*/} = zsh ]] || chsh -s /bin/zsh
