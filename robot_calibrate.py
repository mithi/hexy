from robot import Hexapod

def calibrate_joint(joint, s, mn, mx, z):

    while True:
        for angle in [mn, z, mx, z]:
            joint.move(angle)
            sleep(s)
            
hexy = Hexapod()

#calibrate_joint( hexy.left_back.knee, s = 2, mn = -40, mx = 40, z = 0)

hexy.off()
