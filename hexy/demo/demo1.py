from ..robot.hexapod import Hexapod
from time import sleep

hexy =  Hexapod()

print("lie flat, curl up, then get up")
hexy.boot_up()

print "rotate left"
hexy.rotate(offset = 40)

print "rotate right"
hexy.rotate(offset = -40)

print "walk forward"
hexy.walk(offset = 25, swing = 25)

print "walk backward"
hexy.walk(offset = 25, swing = -25)

print "lie down, lie flat, curl up, and die"
hexy.shut_down()
