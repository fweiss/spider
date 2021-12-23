# Network configuration
Instructions and tips for configuring the network.

You'll nedd the following login access:
- need access to router config
- need access to Name server for your domain

High level:
- static IP on LAN
- port forwarding on router
- DNS to router's WAN IP address
- setup SSL certificate

## Static LAN IP address
This is an optional section, but highly recommended.
If you skip this section, you router could assign a different IP address
later on, and the connection to the server cannot be made.

Steps depend on your router.
> Usually this will be under the DHCP section

## Port forwarding
- need access to router config
- pick a port to open HTTP/80 and HTTPS/443
- use the router console to add the two port forward

Example, assuming RPI is at 192.168.1.100 on the LAN:
```
HTTP[TCP/80-80]->192.168.1.100 [Enabled]
HTTPS[TCP/443-443]->192.168.1.100 [Enabled]
```

## DNS
You've chosen a domain name...
- need access to Name server for your domain
- pick a port to open
- open the port on the router

> make sure you have remote management disabled

The details for this setp vary depending on how you want
to manage your domains and DNS.
The main point is the get the WWW DNS system to resolve the chosen hostname.

Steps:
- get the router WAN address
- create A record in DNS
- point node name (URL) to router's WAN IP

TODO example.

> The defaults for the other settings are usually ok.

## Steps for SSL
This has been automated with Ansible.
