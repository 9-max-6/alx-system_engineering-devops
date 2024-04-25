#!/usr/bin/env bash
# A script to output the length of the content

curl -si $1 | grep "Content-Length" | grep -o '[0-9]\+'
