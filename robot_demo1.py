from robot import Hexapod
from time import sleep

hexy =  Hexapod()
    
print("lie flat, curl up, then get up")
hexy.boot_up()
hexy.default()

print "rotate left"
hexy.rotate(offset = 40)
hexy.default()

print "rotate right"
hexy.rotate(offset = -40)
hexy.default()

print "walk forward"
hexy.walk(offset = 25, swing = 25)
hexy.default()

print "walk backward"
hexy.walk(offset = 25, swing = -25)
hexy.default()

print "lie down, lie flat, curl up, and die"
hexy.shut_down()
