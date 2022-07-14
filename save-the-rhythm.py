from __future__ import unicode_literals
from pathlib import Path
from os import path
import youtube_dl
import argparse
import sys
import os

#Arguments for script
parser = argparse.ArgumentParser(
    prog='Save the Rhtyhm',
    description='Easily download and save Youtube videos as MP3 files.'
)
parser.add_argument('ytlink') #Positional argument containing Youtube link
parser.add_argument('-t', '--title')
parser.add_argument('-d', '--dir') #Optional argument for saving to a specific directory
args = parser.parse_args()

#Settings for download
HOME_DIR = os.path.expanduser('~')
dir = args.dir if args.dir is not None \
    else HOME_DIR

filename = args.title + '.%(ext)s' if args.title is not None \
    else '%(title)s.%(ext)s'

save_path = os.path.join(HOME_DIR, 'Documents', 'audio', filename)

print(f"Saving audio file to {save_path}")

download_settings = {
    'format': 'bestaudio/best',
    'outtmpl': save_path,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }],
}
with youtube_dl.YoutubeDL(download_settings) as ydl:
    ydl.download([args.ytlink])
