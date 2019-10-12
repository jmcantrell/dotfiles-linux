init: submodules install config

submodules:
	git submodule update --init --recursive
	git submodule foreach git checkout master

update:
	git pull --recurse-submodules origin master

install:
	sh ./scripts/install.sh

config:
	sh ./scripts/config.sh

stow:
	stow --no-folding -d . -t $$HOME -R stow

unstow:
	stow --no-folding -d . -t $$HOME -D stow

.PHONY: install config
