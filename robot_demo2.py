from robot_pro import HexapodPro

hexy =  HexapodPro()

hexy.boot_up()
hexy.rest()

hexy.rock_body()
hexy.rest()

hexy.dance_twist()
hexy.rest()

hexy.shake_head()
hexy.rest()

hexy.point(s = 0.75)
hexy.rest()

hexy.type_stuff()
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
