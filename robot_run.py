from robot import Hexapod
from time import sleep

r = 3
s = 1

hexy =  Hexapod()


hexy.lie_flat()
hexy.curl_up()
hexy.lie_flat()
hexy.get_up()
hexy.walk_forward()
hexy.twist_hip()
hexy.lie_down()

hexy.lie_flat()
hexy.curl_up()
sleep(s)

hexy.off()
