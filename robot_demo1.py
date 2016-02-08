from robot import Hexapod
from time import sleep

hexy =  Hexapod()
    
print("lie flat, curl up, then get up")
hexy.boot_up()
hexy.rest()

print "rotate left"
hexy.rotate(offset = 40)
hexy.rest()

print "rotate right"
hexy.rotate(offset = -40)
hexy.rest()

print "walk forward"
hexy.walk(offset = 25, swing = 25)
hexy.rest()

print "walk backward"
hexy.walk(offset = 25, swing = -25)
hexy.rest()

print "lie down, lie flat, curl up, and die"
hexy.shut_down()
