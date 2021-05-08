submodules:
	git submodule update --init --recursive --remote

update:
	git pull
	git submodule foreach git checkout master
	git submodule foreach git pull

stow:
	stow --no-folding -d stow -t ~ -R dotfiles

unstow:
	stow --no-folding -d stow -t ~ -D dotfiles

.PHONY: stow
