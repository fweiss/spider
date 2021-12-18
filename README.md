# denpifs
Distributed network, Raspberry Pi file server

## Hardware
Using a RPI4 platform with NVMe SSD.

- CM4
- WaveShare IO board
- SSD

## Software
Software is provisioned via Ansible.

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

## fancontrol
``sudo apt install fancontrol``





