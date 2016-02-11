from robot_pro import HexapodPro

hexy =  HexapodPro()

hexy.boot_up()

hexy.rock_body()
hexy.default()

hexy.dance_twist()
hexy.default()

hexy.shake_head()
hexy.default()

hexy.point(s = 0.75)
hexy.default()

hexy.type_stuff()
hexy.default()

hexy.wave()
hexy.default()

hexy.tilt_left_and_right()
hexy.tilt_front_and_back()
hexy.default()

hexy.dance_tilt_ccw()
hexy.dance_tilt_cw()
hexy.dance_tilt()
hexy.default()

hexy.shut_down()
