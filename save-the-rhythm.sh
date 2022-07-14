#!bin/bash
youtube-dl --rm-cache-dir
python save-the-rhythm.py "$@"
