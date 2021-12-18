## Fan
Noctua
NF-A3x10
size: 40x10
5V PWM
70 mA
rpm 1000-5000

https://noctua.at/pub/media/wysiwyg/Noctua_PWM_specifications_white_paper.pdf

1 black GND RPI-6
2 yellow +5V RPI-4
3 green SENSE (OC 5mA) RPI-?
4 blue PWM RPI-8

``sudo raspi-config``

Performance Options > Fan
Enable > Yes
GPIO 14
Temperature 60-120 (80)

> On CM4-IO-BASE, the fan PWM is GPIO18
