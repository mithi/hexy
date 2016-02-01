from robot import Hexapod
from time import sleep

r = 3
s = 1

hexy =  Hexapod()

hexy.lie_flat()
sleep(s)
hexy.get_up()

sleep(5)
hexy.off()
