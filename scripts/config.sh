#!/usr/bin/env sh

set -e

# only if allowed to use sudo
if groups | grep -wq wheel; then

    # disable pc speaker
    echo "blacklist pcspkr" | sudo tee /etc/modprobe.d/pcspkr.conf

fi

# change shell to zsh
test ${SHELL##*/} = zsh || chsh -s /bin/zsh
