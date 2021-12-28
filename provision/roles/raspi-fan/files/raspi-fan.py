#!/usr/bin/python3.9

from gpiozero import PWMLED
import RPi.GPIO as GPIO
from time import sleep
import signal
import sys
from collections import namedtuple

FAN_PWM_PIN = 18
UPDATE_INTERVAL = 5

ThermalStatus = namedtuple("ThermalStatus", [ "temp", "clock" ])
Interval = namedtuple("Interval", [ "left", "right" ])

# alias that represents its use
class PWMFan(PWMLED):
    pass

def main():
    signal.signal(signal.SIGINT, handler_stop_signals)
    signal.signal(signal.SIGTERM, handler_stop_signals)

    global fanControl
    fanControl = RpiGpioFanControl()
    monitor = Monitor()
    try:
        ts = monitor.get()
        fanControl.update(ts)
        print("temp: {} fan: {} cpu clock: {}".format(ts.temp, fanControl.duty, ts.clock))
        while True:
            sleep(UPDATE_INTERVAL)
            ts = monitor.get()
            fanControl.update(ts)
            print("temp: {} fan: {} cpu clock: {}".format(ts.temp, fanControl.duty, ts.clock))
    finally:
        pass

def handler_stop_signals(signum, frame):
    try:
        fanControl.cleanup()
    finally:
        sys.exit(0)


# just the logic of getting the desired duty cycle
class BaseFanControl:
    def __init__(self):
        self.duty = 0
        self.tempInterval = Interval(45000, 80000)
        self.dutyInterval = Interval(0.0, 1.0)

    def tempToDuty(self, temp):
        val = self.dutyInterval.left \
                + (self.dutyInterval.right - self.dutyInterval.left) \
                * (temp - self.tempInterval.left) \
                / (self.tempInterval.right - self.tempInterval.left)
        val = max(val, self.dutyInterval.left)
        val = min(val, self.dutyInterval.right)
        return val

class ZeroGpioFanControl(BaseFanControl):
    def __init__(self):
        super().__init__()
        self.fan = PWMFan(FAN_PWM_PIN)

    def update(self, ts):
        self.duty = self.tempToDuty(ts.temp)
        # print("temp: {} duty: {}".format(ts.temp, self.duty))
        # fixem catch error
        self.fan.value = self.duty

    def cleanup(self):
        pass



class RpiGpioFanControl(BaseFanControl):
    def __init__(self):
        super().__init__()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(FAN_PWM_PIN, GPIO.OUT)
        self.fan = GPIO.PWM(FAN_PWM_PIN, 100)
        self.fan.start(100)

    def update(self, ts):
        self.duty = self.tempToDuty(ts.temp)
        self.fan.ChangeDutyCycle(self.duty * 100)

    def cleanup(self):
        print("cleaning up")
        # let the pin go high for default max fan speed
        # on Waveshare IO, GPIO18 is pulled up on board
        # GPIO.setup(FAN_PWM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.cleanup([ FAN_PWM_PIN ])



class Monitor:
    def get(self):
        return ThermalStatus(self.get_temp(), self.get_clock())

    def get_temp(self):
         f = open(r"/sys/class/thermal/thermal_zone0/temp")
         val = f.readline()
         f.close()
         return int(val.strip())

    def get_clock(self):
        f = open(r"/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq")
        val = f.readline()
        f.close()
        return int(val.strip())

if __name__ == "__main__":
    main()
