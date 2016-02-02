from robot import Hexapod
from time import sleep

r = 3
s = 1

hexy =  Hexapod()


hexy.lie_flat()
hexy.curl_up()
hexy.lie_flat()
hexy.get_up()

print "offset = 25, hip_swing = 25"
hexy.walk_forward(offset = 25, hip_swing = 25)
sleep(s)

print "offset = 25, hip_swing = -25"
hexy.walk_forward(offset = 25, hip_swing = -25)
sleep(s)

print "offset = -25, hip_swing = 25"
hexy.walk_forward(offset = -25, hip_swing = 25)
sleep(s)

print "offset = -25, hip_swing = -25"
hexy.walk_forward(offset = -25, hip_swing = -25)
sleep(s)


hexy.twist_hip()
hexy.lie_down()

hexy.lie_flat()
hexy.curl_up()
sleep(s)

hexy.off()
