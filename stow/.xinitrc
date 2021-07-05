#!/usr/bin/env sh

for file in /etc/X11/xinit/.Xresources ~/.Xresources; do
    test -f "$file" && xrdb -merge "$file"
done

for file in ~/.xprofile.d/* /etc/X11/xinit/xinitrc.d/* ~/.xinitrc.d/*; do
    test -f "$file" && . "$file"
done

unset file

exec "${DESKTOP?}"
