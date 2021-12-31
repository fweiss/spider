# spider
Raspberry Pi file server

## Hardware
Using a RPI4 platform with NVMe SSD.

- CM4 Lite 8GB no WiFi/BT
- WaveShare Mini Base Board (A) with M.2 socket
- NVMe SSD size 2242 up to 2TB
- Waveshare CM4 IO BASE BOX and 4-pin fan

![Raspberry Pi Server](case.png)

## Software
Software is provisioned via Ansible.
In this way, the installation and configuration is automated and repeatable.

- custom raspi-fan speed control service
- Apache2 web server
- certbot/Let's Encrypt SSL
- PHP 8.0
- MariaDB
- NodeJS
- Networked A-Frame VR server

## Setup overview
- prepare EEPROM for booting from USB/NVME
- load the OS onto SSD
- setup Ansible playbook parameters
- run the playbook

### Prepare EEPROM for booting from USB/NVME
Follow the details in [NVME](NVME.md).
This only has to be done once for the Raspberry Pi 4 B or CM4.

### Install the target OS image
There are several ways to put a Raspberry Pi OS image on an SDcard or SSD.
For reference, this is the process I used:
- launch Raspberry Pi Imager
- select Other general purpose OS > Ubuntu > Ubuntu Server 21.10 (RPI 3/4/400) 64-bit server OS for arm64 architectures
- select the SDCard or SSD
- click Write

> See notes in [NVME](NVME.md) for reason Ubuntu Server 21.10 was chosen.

After the image is written and verfied, make sure to enable ssh.

> On Mac, run ``touch /Volumes/system-boot/ssh``

## Setup Ansible playbook parameters
Install Ansible, etc.
- find the RPI IP address from DHCP
- ssh and confirm fingerprint
- recommend change password or set cert auth
- you should be able to login with password

> If you've forgotten how: [Two simple steps for passwordless ssh](https://www.linuxbabe.com/linux-server/setup-passwordless-ssh-login)

## Run the Ansible playbook
Checklist:
- passwordless login to target RPI
- DNS routes hostname DNS address to router WAN IP address
- router forwards HTTP and HTTPS to target IP address

Run the playbook:
``ansible-playbook -i hosts playbook.yml``

> Initial play: about 15 minutes??, repeat play about 3 minutes.

## Cooling performance
```
sudo apt update
sudo apt install sysbench
sysbench --num-threads=4 --test=cpu --cpu-max-prime=20000 --validate run
/opt/vc/bin/vcgencmd measure_temp
```

## Stress testing temperature
https://core-electronics.com.au/tutorials/how-to-stress-test-temperature-on-raspberry-pi.html

## Provisioning with Ansible
https://coderwall.com/p/6zm8rq/how-to-create-a-lamp-stack-with-ansible

Install Ansible on Windows 10 with WSL: https://phoenixnap.com/kb/install-ansible-on-windows#htoc-method-3-enabling-ubuntu-on-windows

> The windows drives are at /mnt, e,g, ``/mnt/c``
