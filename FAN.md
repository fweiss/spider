# Fan
The Raspberry Pi has built-in hardware thermal management.
When the chip reaches certain temperature thresholds, it throttles the CPU clock.
Thus the use of a fan is really for CPU clock optimization, not preventing overheating.

## Fan noise

Ways to control fan
- direct GPIO on/off
- PWM GPIO
- I2C control chip (e.g. EMC2301)

## Raspian OS fan control
Raspian OS has a simple PWN fan control built in.
It can be configured with ``raspi-config``.

## Ubuntu fan control
There doesn't seem to be a standard Ubuntu fan control.

## Custom solution of Ubuntu
This project has a Ansible role for a Ubuntu service to control the fan speed.

## Monitoring and testing

temperature: ``cat /sys/class/thermal/thermal_zone0/temp``
cpu clock: sudo cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq


## Observations
Test with custom fancontrol.
Profile was (0.0-1.0)/(45000-80000).
TODO: explore different prfiles.
- run stress test: ``stress -c 4 -t 900s``
- wait for steady state
- 94 Hz = 5,640 RPM (or 1/2?)
- core = 64.5 C
- 52 C @ 22 Hz, 1320 RPM

## Links and references

Python service, but no PWM
https://github.com/Bengreen/pi-fan-controller

Python service with PWM
https://github.com/agarthetiger/argon-one

kernal module for use with EMC2301
https://github.com/neg2led/cm4io-fan

Stress testing
https://core-electronics.com.au/tutorials/stress-testing-your-raspberry-pi.html
