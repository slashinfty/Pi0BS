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

```
passwd
sudo apt update && sudo apt upgrade -y
sudo apt install git pip3
git clone https://github.com/slashinfty/Pi0BS.git
cd Pi0BS
pip3 install -r requirements.txt
sudo usermod -a -G gpio pi
sudo raspi-config (autologin on boot)
nano ~/.bashrc (add python3 /home/pi/Pi0BS/Pi0BS.py &)
```

### Customize the Script
In `Pi0BS.py` you will need to add in the address, port, and password of your OBS websocket. You can also edit any functions using any [requests](https://github.com/Palakis/obs-websocket/blob/4.x-current/docs/generated/protocol.md) from the websocket API.

## Physical Build
Wiring

3D printing
