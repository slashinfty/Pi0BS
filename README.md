# Pi0BS
Control OBS via websocket with a Raspberry Pi Zero W

## Required Materials
* Raspberry Pi Zero W
* Micro SD card
* Micro USB cable
* Buttons (up to 25)

## Setup
This will guide you through setting up the Raspberry Pi and script. It is assumed that you know how to find the IP addresses of machines on your network.

### Operating System
You will be using Raspberry Pi OS Lite. The [Raspberry Pi Imager](https://www.raspberrypi.org/software/) is recommended for downloading and installing the image onto the SD card.

Before booting the Pi, you'll also need to set up SSH and WiFi before booting. Create an empty file with the name `ssh` and place it in the boot drive. Create a file named `wpa_supplicant.conf` in the boot drive, and input the following inside the file:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
    ssid="Your network name/SSID"
    psk="Your WPA/WPA2 security key"
    key_mgmt=WPA-PSK
}
```

Be sure to edit your country code, SSID, and password.

Insert the micro SD card into the Raspberry Pi and boot it up, then log into it via SSH.

First thing you'll want to do it edit your password with the command `passwd`. Then update the system and install a couple of needed applications.

```
sudo apt update && sudo apt -y upgrade
sudo apt -y install git pip3
```

After that is complete, we'll get Pi0BS onto the device.

```
git clone https://github.com/slashinfty/Pi0BS.git
cd Pi0BS
pip3 install -r requirements.txt
```

At this point, it may be useful to edit the `Pi0BS.py` script (see below).

Lastly, we need to ensure we can use the GPIO pins (use the command `sudo usermod -a -G gpio pi`), that the Pi autologins (use the command `sudo raspi-config` and go to System Options), and the script runs at login (use the command `nano ~/.bashrc` and add the line `python3 /home/pi/Pi0BS/Pi0BS.py &` to the bottom).

### Customize the Script
In `Pi0BS.py` you will need to add in the address, port, and password of your OBS websocket.

You can also edit any functions using any [requests](https://github.com/Palakis/obs-websocket/blob/4.x-current/docs/generated/protocol.md) from the websocket API.

Be sure to comment out any buttons that you are not connecting.

## Physical Build
Wiring

3D printing
