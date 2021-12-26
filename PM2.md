# Decoding pm2
I haven't found comprehesive documentation.

Notes are for ubuntu.

``ls -la /etc/systemd/system/pm2*``

``more /etc/systemd/system/pm2-naf.service``

``ls -la ~naf/.pm2``

Evidently ``pm startup ...`` needs to be run as sudo,
but creates separate service for each user.

Run ``pm2 start`` and ``pm2 save`` as the service user.
