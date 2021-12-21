Raspian has a simple PWN fan control built in
Ubuntu?

temperature: ``cat /sys/class/thermal/thermal_zone0/temp``
cpu clock: sudo cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq

stress test: ``stress -c 4 -t 900s``

Python service, but no PWM
https://github.com/Bengreen/pi-fan-controller

Python service with PWM
https://github.com/agarthetiger/argon-one

Ways to control fan
- direct GPIO on/off
- PWM GPIO
- I2C control chip (e.g. EMC2301)

## Links and references
kernal module for use with EMC2301
https://github.com/neg2led/cm4io-fan

Stress testing
https://core-electronics.com.au/tutorials/stress-testing-your-raspberry-pi.html
