# Fan
Information about some fans

## Waveshare Fan-4010-PWM-5V
> The sense period has differencet values depending on sequences
> 
1 black GND
2 red +5V
3 blue SENSE
4 yellow PWM

> Sense is 1 or 2 times per revolution?

### Default (no PWM)
PWM (after power up): high (2.4 V)
SENSE: 5.77 ms, 173.3 Hz, 10,398 RPM

PWM (after stop fancontrol): low
SENSE: 95.6 ms, 10.46 Hz, 627.6 RPM?

> Left fan in low speed!

### raspi config
sense: 
pwm: low

## Waveshare Fan-4010-PWM-12V
- rated speed 5000 rpm
- rated power 0.48W (12V, 0.04±0.02A)


## Noctua NF-A3x10
size: 40x10
5V PWM
70 mA
rpm 1000-5000

https://noctua.at/pub/media/wysiwyg/Noctua_PWM_specifications_white_paper.pdf

1 black GND RPI-6
2 yellow +5V RPI-4
3 green SENSE (OC 5mA) RPI-?
4 blue PWM RPI-8

> RPM 2 pulses per revolution

``sudo raspi-config``

Performance Options > Fan
Enable > Yes
GPIO 14
Temperature 60-120 (80)

> On CM4-IO-BASE, the fan PWM is GPIO18
