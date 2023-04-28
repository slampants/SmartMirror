# Untitled Custom SmartMirror Project

## Basics
The goal of this smart mirror project was to build a smart mirror display from scratch using only Python, with the intention of really only seeing a bare minimum of important information to help me get dressed in the morning:
1. Tell me the weather right now
2. Tell me the next time I can expect a non-trivial amount of rain

And try to not look shitty in the process.

This README deals exclusively with the software side of the project, and will not cover the actual buildout in any way.

## Setup
Some of the nuances of this project are taylored toward the very specific hardware build I'm running, which is with a Raspberry Pi 3.

### Versions
Getting everything to play nicely together was definitely not easy. Most software versioning is accounted for in the `requirements.txt` file, but a couple others of note:
SDL 2.0.14
Python 3.9.2

### Set up the new Pi
Install the full 32 bit version with CLI. For whatever reason this sets things up better.
Enable SSH
Clone the repo onto the device
Make venv with `python -m venv ./venv`

Font support:
sudo apt-get install python3-sdl2 

Install requirements:
- Activate venv
- `pip install -r requirements.txt`

Replace `/boot/config.txt` with /PROJECT_DIRECTORY_HERE/REFS/config.txt
Reboot

Run the app
