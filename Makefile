submodules:
	git submodule update --init --recursive --remote

update:
	git pull
	git submodule foreach git checkout master
	git submodule foreach git pull

install: stow
	rsync -avz ./copy/ ~

stow:
	stow --no-folding -d . -t ~ -R stow

unstow:
	stow --no-folding -d . -t ~ -D stow

.PHONY: stow
