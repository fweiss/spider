# NVMe
Booting an OS via NVMe SSD

## Overview
- update EEPROM bootloader
- load image to SSD
- setup OS
- issues

## CM4 EEPROM bootloader
Raspberry Pi 4, etc., have bootloader in EEPROM.
Early version of CM4 did not have NVMe support in eeprom bootloader.
Need new bootloader, at least July 2021.

Tool for updating EEPROM: https://github.com/raspberrypi/usbboot.

This sets up a virtual boot device for a RPI connected via USB.
It provides an image that updates the EEPROM bootloader.

> Important: also need to set a switch or jumper to allow boot from USB.

### Version before
```shell
> vcgencmd bootloader_version
Feb 16 2021 13:23:36
version d6d82cf99bcb3e9a166a34cfde53130957a36bd3 (release)
timestamp 1613481816
update-time 1613481816
capabilities 0x0000001f

> vcgencmd bootloader_config
[all]
BOOT_UART=0
WAKE_ON_GPIO=1
POWER_OFF_ON_HALT=0

# Try  SD- > USB PCIe MSD -> USB 2.0 BCM XHCI -> Network ->  Loop
BOOT_ORDER=0xf2541

# Set to 0 to prevent bootloader updates from USB/Network boot
# For remote units EEPROM hardware write protection should be used.
ENABLE_SELF_UPDATE=1
```

### Update procedure
- on Mac ``./rpiboot -v -d recovery``
- remove sdcard?
- switch boot to ON (for WaveShare)
- connect HDMI to monitor
- connect mac to RPI USB-C
- ACT LED flashes
- monitor screen turns green
- unplug USB-C
- switch boot to OFF
- bullseye sdcard?
- USB-C power

### Version after
```shell
> vcgencmd bootloader_version
2021/11/22 11:23:32
version 3c912e10a67767dc7867f60ea4c7b75a03485080 (release)
timestamp 1637580212
update-time 1638293518
capabilities 0x0000007f

> sudo vcgencmd bootloader_config
[all]
BOOT_UART=0
WAKE_ON_GPIO=1
POWER_OFF_ON_HALT=0

# Try SD first (1), followed by, USB PCIe, NVMe PCIe, USB SoC XHCI then network
BOOT_ORDER=0xf25641

# Set to 0 to prevent bootloader updates from USB/Network boot
# For remote units EEPROM hardware write protection should be used.
ENABLE_SELF_UPDATE=1
```

## Load OS image on SSD
There was some trial and error.

### Raspian bullseye
worked OK
### Ubuntu 20.4.30 64 bit
- boots from SD
- some boot log
- no desktop on boot
- no USB keyboard
- accepts ssh connection
- 
### Ubuntu Server 21.10 (RPI 3/4/400) 64 bit
- boots from NVMe
- no boot log
- desktop on boot
- no USB mouse + keyboard
- refuses ssh connection

### Latest try
https://connerlabs.org/running-ubuntu-arm64-on-your-raspberry-pi-cm4/

- update eeprom bootloader
- raspberry pi imager Ubuntu 21.10 64 bit

mount and edit
- toucn ssh
- config.txt: enable USB2


lsblk
```
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
mmcblk0     179:0    0  14.8G  0 disk
├─mmcblk0p1 179:1    0   256M  0 part /boot
└─mmcblk0p2 179:2    0  14.6G  0 part /
nvme0n1     259:0    0 119.2G  0 disk
```

sudo blkid
```
/dev/mmcblk0p1: LABEL_FATBOOT="boot" LABEL="boot" UUID="E183-6233" BLOCK_SIZE="512" TYPE="vfat" PARTUUID="da2999b0-01"
/dev/mmcblk0p2: LABEL="rootfs" UUID="1232a209-2596-48f0-a078-731d10b918ad" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="da2999b0-02"
/dev/nvme0n1: PTUUID="47091403-a766-4c38-84c5-d1830b78569d" PTTYPE="gpt"
```

sudo mkdir /mnt/nvme
sudo mount /dev/nvme0n1 /mnt/nvme

> wrong fs type

sudo parted --list

sudo parted /dev/nvme0n1 mkpart primary fat32 0G 100%

 sudo mkfs.ext4 -F -q -L ROOT /dev/nvme0n1p1

sudo mkfs.ext4 /dev/nvme0n1p1

> looks like it had Windows EFI OS.


dd if=/mnt/nvme/test.img of=/dev/zero bs=1G count=50 oflag=dsync
vcgencmd measure_temp

## Booting

``sudo raspi-config`` advanced > bootloader version > latest

https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#nvme-ssd-boot
> The fix was to use a 21.4 kernel and 20.4 userland.

Try Raspberry Pi Imager 1.6.2
Choose OS > Misc utility images > Bootloader > SD card boot

- connect USB mac to rpi
- run rpiboot on mac
- insert sd card with bootloader image
- power up rpi

> Bootloader loops, USB timeout

## New new
```shell
>  sudo CM4_ENABLE_RPI_EEPROM_UPDATE=1 rpi-eeprom-update
*** UPDATE AVAILABLE ***
BOOTLOADER: update available
   CURRENT: Tue 16 Feb 13:23:36 UTC 2021 (1613481816)
    LATEST: Mon 22 Nov 11:23:32 UTC 2021 (1637580212)
   RELEASE: stable (/lib/firmware/raspberrypi/bootloader/stable)
            Use raspi-config to change the release.

  VL805_FW: Using bootloader EEPROM
     VL805: up to date
   CURRENT:
    LATEST:
```

Then with -a
reboot

> damnit! still doesn't work

## 2012-12-10
```shell
>  sudo CM4_ENABLE_RPI_EEPROM_UPDATE=1 -E rpi-eeprom-update
*** UPDATE AVAILABLE ***
BOOTLOADER: update available
   CURRENT: Tue 16 Feb 13:23:36 UTC 2021 (1613481816)
    LATEST: Mon 22 Nov 11:23:32 UTC 2021 (1637580212)
   RELEASE: stable (/lib/firmware/raspberrypi/bootloader/stable)
            Use raspi-config to change the release.

  VL805_FW: Using bootloader EEPROM
     VL805: up to date
   CURRENT:
    LATEST:
```

```shell
sudo raspi-config > advanced > bootloader version > latest
do not revert to default?
```

```

Raspberry Pi Desktop
SD Card Copier


## Links and references
https://forums.raspberrypi.com/viewtopic.php?t=306507&start=25







