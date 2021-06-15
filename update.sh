#!/usr/bin/env bash

set -e

export PATH=$PWD/bin:$PATH

git pull
git submodule update --init
git submodule foreach git checkout master
