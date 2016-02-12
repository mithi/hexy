from ..robot.dancing import DancingHexapod
from time import sleep

hexy = DancingHexapod()

sleep(3)

hexy.boot_up()
hexy.default()

hexy.night_fever()
hexy.default()

hexy.thriller()
hexy.default()

hexy.shut_down()
    
