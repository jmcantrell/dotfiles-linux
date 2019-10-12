init: install config

install:
	sh ./scripts/install.sh

config:
	sh ./scripts/config.sh

stow:
	stow --no-folding -d . -t $$HOME -R stow
unstow:
	stow --no-folding -d . -t $$HOME -D stow

.PHONY: install config
