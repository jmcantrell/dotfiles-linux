#!/usr/bin/env sh

export DESKTOP=i3
export VISUAL=gvim
export BROWSER=firefox
export TERMINAL=xterm
export TERMCMD=$TERMINAL

for xresources in /etc/X11/xinit/.Xresources ~/.Xresources; do
    test -f "$xresources" && xrdb -merge "$xresources"
done
unset xresources

for d in /etc/X11/xinit/xinitrc.d ~/.xinitrc.d; do
    for f in "$d"/*; do
        test -f "$f" && . "$f"
    done
    unset f
done
unset d

exec "$DESKTOP"
