from robot import Hexapod
from time import sleep

hexy =  Hexapod()

s = 0.5

hexy.lie_flat()
hexy.curl_up()
hexy.get_up()

hexy.pose_attention()
sleep(s)

print "rotate left offset = 40"
hexy.rotate(offset = 40)

hexy.pose_attention()
print "rotate right offset = -40 right"
hexy.rotate(offset = -40)

print "walk offset = 25, hip_swing = 25 forward"
hexy.walk(offset = 25, hip_swing = 25)
sleep(s)

print "walk offset = 25, hip_swing = -25 backward"
hexy.walk(offset = 25, hip_swing = -25)
sleep(s)

print "walk offset = -25, hip_swing = 25 forward"
hexy.walk(offset = -25, hip_swing = 25)
sleep(s)

print "walk offset = -25, hip_swing = -25 backward"
hexy.walk(offset = -25, hip_swing = -25)
sleep(s)

hexy.twist_hip()
hexy.lie_down()

hexy.lie_flat()
hexy.curl_up()
sleep(s)

hexy.off()
