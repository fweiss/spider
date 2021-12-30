# spider
Distributed network, Raspberry Pi file server

## Hardware
Using a RPI4 platform with NVMe SSD.

- CM4
- WaveShare IO board
- SSD

## Software
Software is provisioned via Ansible.

## Setup overview
- prepare EEPROM for booting from USB/NVME
- load the OS onto SSD
- setup Ansible playbook parameters
- run the playbook

## Setup Ansible playbook parameters
- find the RPI IP address from DHCP
- ssh and confirm fingerprint
- recommend change password or set cert auth
- first check ssh

## Run the Ansible playbook
Checklist:
- passwordless login to target RPI
- DNS routes hostname DNS address to router WAN IP address
- router forwards HTTP and HTTPS to target IP address

Run the playbook:
``ansible-playbook -i hosts playbook.yml``

> If you've forgotten how: [Two simple steps for passwordless ssh](https://www.linuxbabe.com/linux-server/setup-passwordless-ssh-login)


## Performance
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
