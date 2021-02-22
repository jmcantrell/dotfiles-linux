#!/usr/bin/env sh

export DESKTOP=i3
export VISUAL=gvim
export BROWSER=vimb
export TERMINAL=xterm

# x resources
for xresources in /etc/X11/xinit/.Xresources ~/.Xresources; do
	test -f "$xresources" && xrdb -merge "$xresources"
done

# keyboard mappings
for xmodmap in /etc/X11/xinit/.Xmodmap ~/.Xmodmap; do
	test -f "$xmodmap" && xmodmap "$xmodmap"
done

# auto start scripts
for d in /etc/X11/xinit/xinitrc.d ~/.xinitrc.d; do
	for xinitrc in "$d"/*; do
		test -f "$xinitrc" && . "$xinitrc"
	done
done

exec "$DESKTOP"
