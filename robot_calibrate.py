from robot import Hexapod
from time import sleep

def calibrate_joint(joint, s, mn, mx, z):

    while True:
        for angle in [mn, z, mx, z]:
            joint.move(angle)
            sleep(s)
            
hexy = Hexapod()

#calibrate_joint( hexy.neck, s = 2, mn = -90, mx = 90, z = 0)

hexy.off()
