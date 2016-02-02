from robot import Hexapod
from time import sleep

r = 3
s = 1

hexy =  Hexapod()


hexy.lie_flat(s)

hexy.curl_up(s)

hexy.lie_flat(s)

hexy.get_up()
sleep(s)

hexy.walk_forward()

sleep(5)
hexy.off()
