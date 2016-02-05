from robot import Hexapod
from time import sleep


hexy =  Hexapod()

hexy.boot_up()
hexy.rest()

hexy.shake_head()
hexy.rest()

hexy.point(s = 0.75)
hexy.rest()

hexy.type_stuff()
hexy.rest()

hexy.twist_hip_slowly()
hexy.rest()

hexy.wave()
hexy.rest()

hexy.tilt_left_and_right()
hexy.rest()

hexy.tilt_front_and_back()
hexy.rest()

hexy.dance_tilt_ccw()
hexy.rest()

hexy.dance_tilt_cw()
hexy.rest()

hexy.dance_tilt()
hexy.rest()

hexy.shut_down()
