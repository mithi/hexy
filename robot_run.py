from robot import Hexapod
from time import sleep

r = 3
s = 1

hexy =  Hexapod()


hexy.lie_flat()
hexy.curl_up()
hexy.lie_flat()
hexy.get_up()

for angle in xrange(-40, 40, 5):
    hexy.twist_hip(angle, 0.01)

for angle in xrange(40, -40, -5):
    hexy.twist_hip(angle, 0.01)

hexy.twist_hip()

print "offset = 40 forward"
hexy.rotate(offset = 40)

print "offset = -40 backward"
hexy.rotate(offset = -40)

'''
print "offset = 25, hip_swing = 25 forward"
hexy.walk(offset = 25, hip_swing = 25)
sleep(s)

print "offset = 25, hip_swing = -25 backward"
hexy.walk(offset = 25, hip_swing = -25)
sleep(s)

print "offset = -25, hip_swing = 25 forward"
hexy.walk(offset = -25, hip_swing = 25)
sleep(s)

print "offset = -25, hip_swing = -25 backward"
hexy.walk(offset = -25, hip_swing = -25)
sleep(s)
'''

hexy.twist_hip()
hexy.lie_down()

hexy.lie_flat()
hexy.curl_up()
sleep(s)

hexy.off()
