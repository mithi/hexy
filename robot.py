from core_robot import HexapodCore
from time import sleep

class Hexapod(HexapodCore):

    def lie_flat(self, s = 0.1):
        
        for leg in self.legs:
            leg.move()
            
        sleep(s)

    def stretch(self, hip_angle = 0, s = 0.1):
        # hip_angle > 0 points toward front else points towards side
        
        self.right_front.hip.move(hip_angle)
        self.right_back.hip.move(-hip_angle)
        self.right_middle.hip.move()
        
        self.left_front.hip.move(-hip_angle)
        self.left_middle.hip.move()
        self.left_back.hip.move(hip_angle)
        
        sleep(s)

    def get_up(self, maxx = 50):
        
        angles = range(-maxx, maxx + 1)

        for angle in angles:
            for leg in self.legs:
                leg.step(angle)        

    def twist_hip(self, angle = 0, s = 0.1):

        for hip in self.hips:
            hip.move(angle)

        sleep(s)   

def calibrate_joint(joint, s, mn, mx, z):

    while True:
        for angle in [mn, z, mx, z]:
            joint.move(angle)
            sleep(s)

hexy = Hexapod()
#calibrate_joint( hexy.right_back.ankle, s = 2, mn = -90, mx = 90, z = 0)

