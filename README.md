# dotfiles-linux

My configuration files and scripts common to all Linux distributions.

## Installation

Clone this repository:

```sh
git clone git@gitlab.com:jmcantrell/dotfiles-linux.git ~/.dotfiles-linux
cd ~/.dotfiles-linux
```

Symlink files, install packages, and configure system:

```sh
./scripts/stow
./scripts/install
./scripts/config
```

Update repository with the latest changes:

```sh
./scripts/update
```

Remove files from home directory:

```sh
./scripts/unstow
```
