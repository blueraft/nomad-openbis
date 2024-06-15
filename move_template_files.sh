#!/bin/sh

rsync -avh nomad-openbis/ .
rm -rfv nomad-openbis
