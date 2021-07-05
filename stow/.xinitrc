#!/usr/bin/env sh

for file in /etc/X11/xinit/.Xresources ~/.Xresources; do
    test -r "$file" && xrdb -merge "$file"
done

for file in ~/.xprofile.d/*; do
    test -r "$file" && . "$file"
done

for file in /etc/X11/xinit/xinitrc.d/* ~/.xinitrc.d/*; do
    test -x "$file" && "$file"
done

unset file

exec "${DESKTOP?}"
