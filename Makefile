init: install config

update:
	git pull origin master
	git submodule update --init --recursive
	git submodule foreach git pull origin master

install:
	sh ./scripts/install.sh

config:
	sh ./scripts/config.sh

stow:
	stow --no-folding -d . -t $$HOME -R stow

unstow:
	stow --no-folding -d . -t $$HOME -D stow

.PHONY: install config
