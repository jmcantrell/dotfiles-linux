#!/usr/bin/env bash

for file in /etc/X11/xinit/.Xresources ~/.Xresources; do
    [[ -r $file ]] && xrdb -merge "$file"
done

for file in ~/.xprofile.d/* /etc/X11/xinit/xinitrc.d/* ~/.xinitrc.d/*; do
    [[ -r $file ]] && . "$file"
done

unset file

exec "${DESKTOP?}"
