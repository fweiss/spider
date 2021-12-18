## Ubuntu
Raspberry Pi Imager
Ubuntu 20.04.3 LTS 64
plus Desktopify

## NAF
What is mtools needed for?
```
mkdir NAF
cd NAF
sudo apy install git
git clone https://github.com/networked-aframe/networked-aframe.git
cd networked-aframe
npm install --only=prod
node ./server/easyrtc-server.js
```

> The npm install takes a while. Use --only=prod instead.
> Need to use dev environment?

## NAF self-signed
``openssl req -nodes -new -x509 -keyout server.key -out server.cert``
common name: raspberrypi.local
