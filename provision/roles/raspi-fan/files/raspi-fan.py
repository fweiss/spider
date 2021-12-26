#!/usr/bin/python3.9

from gpiozero import PWMLED
from time import sleep
from collections import namedtuple

UPDATE_INTERVAL = 5

ThermalStatus = namedtuple("ThermalStatus", [ "temp", "clock" ])
Interval = namedtuple("Interval", [ "left", "right" ])

# alias that represents its use
class PWMFan(PWMLED):
    pass

def main():
    fanControl = FanControl()
    monitor = Monitor()
    ts = monitor.get()
    fanControl.update(ts)
    print("temp: {} fan: {} cpu clock: {}".format(ts.temp, fanControl.duty, ts.clock))
    while True:
        sleep(UPDATE_INTERVAL)
        ts = monitor.get()
        fanControl.update(ts)
        print("temp: {} fan: {} cpu clock: {}".format(ts.temp, fanControl.duty, ts.clock))

class FanControl:
    def __init__(self):
        self.fan = PWMFan(18)
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

    def update(self, ts):
        self.duty = self.tempToDuty(ts.temp)
        # print("temp: {} duty: {}".format(ts.temp, self.duty))
        # fixem catch error
        self.fan.value = self.duty

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
