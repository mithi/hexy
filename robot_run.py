from robot import Hexapod
from time import sleep

r = 3
s = 1

hexy =  Hexapod()


hexy.lie_flat()
hexy.curl_up()
hexy.lie_flat()

hexy.get_up()

for i in xrange(2):

    for angle in xrange(-45, 45, 3):
        hexy.twist_hip(angle, 0.01)

    for angle in xrange(45, -45, -3):
        hexy.twist_hip(angle, 0.01)

hexy.twist_hip()

hexy.pose_attention()
sleep(0.3)

hexy.type_stuff()
sleep(0.3)

hexy.pose_attention()
sleep(0.3)

hexy.shake_head()
sleep(0.3)

hexy.point()
sleep(0.3)

hexy.pose_attention()

print "tilt right"
hexy.tilt_side(left_angle = 50, right_angle = 0, s = 1)

print "tilt left"
hexy.tilt_side(left_angle = 0, right_angle = 50, s = 1)

print "tilt front"
hexy.tilt(front_angle = 0, middle_angle = 25, back_angle = 50, s = 1)

print "tilt back"
hexy.tilt(front_angle = 50, middle_angle = 25, back_angle = 25, s = 1)

hexy.pose_attention()

hexy.twist_hip()
hexy.lie_down()

hexy.lie_flat()
hexy.curl_up()
sleep(s)

hexy.off()
