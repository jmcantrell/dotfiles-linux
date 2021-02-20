#!/usr/bin/env bash

export DESKTOP=i3
export VISUAL=gvim
export BROWSER=vimb
export TERMINAL=xterm

# x resources
for xresources in {/etc/X11/xinit,"$HOME"}/.Xresources; do
    test -f "$xresources" && xrdb -merge "$xresources"
done

# keyboard mappings
for xmodmap in {/etc/X11/xinit,"$HOME"}/.Xmodmap; do
    test -f "$xmodmap" && xmodmap "$xmodmap"
done

# auto start scripts
for d in /etc/X11/xinit/xinitrc.d "$HOME"/.xinitrc.d; do
    for xinitrc in "$d"/*; do
        test -x "$xinitrc" && source "$xinitrc"
    done
done

exec "$DESKTOP"
