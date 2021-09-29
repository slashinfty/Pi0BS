# Pi0BS
Control OBS via websocket with a Raspberry Pi Zero W

## Required Materials
* Raspberry Pi Zero W
* Micro SD card
* Micro USB cable
* LED & 330 ohm resistor (optional)
* Buttons (up to 25)

## Setup
This will guide you through setting up the Raspberry Pi and script.

### Operating System
Download Raspberry Pi OS Lite from [raspberrypi.org](https://www.raspberrypi.org/software/operating-systems/). The [Raspberry Pi Imager](https://www.raspberrypi.org/software/) is recommended for getting the image onto the SD card.

You'll also need to set up SSH (see below) and [WiFi](https://www.raspberrypi.org/documentation/computers/configuration.html#setting-up-a-headless-raspberry-pi) before booting.

> For headless setup, SSH can be enabled by placing a file named ssh, without any extension, onto the boot partition of the SD Card. When the Raspberry Pi boots, it looks for the ssh file. If it is found, SSH is enabled and the file is deleted. The content of the file does not matter; it could contain text, or nothing at all. 

### Customize the Script
In `Pi0BS.py` you will need to add in the address, port, and password of your OBS websocket. You can also edit any functions using any [requests](https://github.com/Palakis/obs-websocket/blob/4.x-current/docs/generated/protocol.md) from the websocket API.

### Script at Boot



## Physical Build
Wiring

3D printing
