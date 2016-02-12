from ..robot.pro import HexapodPro
from time import sleep

hexy =  HexapodPro()

sleep(5)

hexy.boot_up()

hexy.rock_body()
hexy.default()

hexy.dance_twist()
hexy.default()

hexy.shake_head()
hexy.default()

hexy.point()
hexy.default()

hexy.type_stuff()
hexy.default()

hexy.wave()
hexy.default()

hexy.tilt_left_and_right()
hexy.default()

hexy.tilt_front_and_back()
hexy.default()

hexy.dance_tilt()
hexy.default()

hexy.shut_down()
