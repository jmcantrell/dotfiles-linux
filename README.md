# dotfiles-linux

My configuration files and scripts common to all Linux distributions.

## Installation

Clone this repository:

```sh
git clone git@gitlab.com:jmcantrell/dotfiles-linux.git ~/.dotfiles-linux
cd ~/.dotfiles-linux
```

Install packages, symlink files, and configure system:

```sh
./scripts/install
./scripts/stow
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
