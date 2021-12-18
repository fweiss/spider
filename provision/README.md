# Provisioning with Ansible
The playbook will provision the Raspberry Pi with:
- apache2
- php 8.0
- mariadb

> Coming soon: apache2/SSL, drupal, fan control

## Setup Ansible
There are [several methods](https://phoenixnap.com/kb/install-ansible-on-windows) to setup Ansible on Windows.
I chose the WSL (Windows Subsystem for Linux) method because it seems to be the simplest.

## Running the playbook
Run the playbook from the command line:
```shell
cd provision
ansible-playbook -i hosts playbook.yml
```

## Check the finished system
results:
- http://server => apache info
- http://server/index.php => hello world
- http://server/db.php => Hello World!

> Todo: SSL, drupal NAF

## Notes and references
additional packages required for ansible:


sudo apt install python3-pip
sudo pip3 install pymsql

> nope, these go on the target
> 
> Nope again, neded for ansible module
> sudo apt-get install python3-pymysql

add become: yes instead of --sudo on the command line

couldn't use dns raapberrypi, had to use ipv6

on wsl:
sudo apt-get install python3-pymysql
already newest version
but what about ansible plugin?

sudo apt-get install python3-mysqldb?
nope

on WSL:
``The PyMySQL (Python 2.7 and Python 3.X) or MySQL-python (Python 2.X) module is required.``

galaxy is now working:
``ansible-galaxy collection list``

so,
``ansible-galaxy collection install community.mysql``

``export ANSIBLE_KEEP_REMOTE_FILES=1``

## synopsis
- on W10, enable WSL
- from Windows store, get ubuntu 20.4
- install ansible, etc
- cd to project directory /mnt/*
- 


