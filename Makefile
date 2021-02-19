submodules:
	git submodule update --init --recursive

update:
	git pull --recurse-submodules

install:
	sh ./scripts/install.sh

config:
	sh ./scripts/config.sh

stow:
	stow --no-folding -d stow -t ~ -R dotfiles

unstow:
	stow --no-folding -d stow -t ~ -D dotfiles

.PHONY: install config stow
