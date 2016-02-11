from robot import Hexapod
from time import sleep

def calibrate_joint(joint, t, mn, mx, z):

    while True:
        for angle in [mn, z, mx, z]:
            joint.pose(angle)
            sleep(t)
            
hexy = Hexapod()
#calibrate_joint( hexy.right_back.knee, t = 2, mn = -45, mx = 45, z =0)
hexy.off()
