from robot import Hexapod
from time import sleep

def calibrate_joint(joint, s, mn, mx, z):

    while True:
        for angle in [mn, z, mx, z]:
            joint.move(angle)
            sleep(s)
            
hexy = Hexapod()

#calibrate_joint( hexy.right_back.hip, s = 2, mn = -45, mx = 45, z = 0)
    
hexy.off()
