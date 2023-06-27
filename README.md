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
- SDL 2.0.14
- Python 3.9.2

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

Replace the pi's `/boot/config.txt` with `/PROJECT_DIRECTORY_HERE/REFS/config.txt`

To stop the `hwmon` low voltage warning messages from printing to the console, which kills the app, add:
```
sudo dmesg -n 1
```
to `/etc/rc.local`
(src: https://askubuntu.com/questions/97256/how-do-i-disable-messages-or-logging-from-printing-on-the-console-virtual-termin/97318#97318)

And modify `/etc/sysctl.conf`:
```
# Uncomment the following to stop low-level messages on console
#kernel.printk = 3 4 1 3    <-------- UNCOMMENT THIS LINE
```
(src: https://superuser.com/questions/351387/how-to-stop-kernel-messages-from-flooding-my-console)

Reboot

Run the app
