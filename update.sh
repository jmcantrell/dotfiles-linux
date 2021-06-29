#!/usr/bin/env sh

set -e

git checkout master
git pull origin master
git submodule update --remote
