from core_robot import HexapodCore
from time import sleep

class Hexapod(HexapodCore):

    def curl_up(self, s = 0.2, die = False):

        for leg in self.legs:
            leg.hip.move(0)
            leg.knee.move(-leg.knee.max)
            leg.ankle.move(leg.ankle.max)

        sleep(s)

        if die: self.off()

    def lie_flat(self, s = 0.2):
        
        for leg in self.legs:
            leg.move()
            
        sleep(s)

    def get_up(self, maxx = 50, step = 4, s = 0.2):

        for angle in xrange(-maxx, maxx + 1, step):
            for leg in self.legs:
                leg.step(angle)

        sleep(s)

    def twist_hip(self, angle = 0, s = 0.2):

        for hip in self.hips:
            hip.move(angle)

        sleep(s)

    def walk_forward(self, offset = 25 , hip_swing =  20, raised = -30, floor = 50, repetitions = 3):

        first_swing = [offset - hip_swing, hip_swing, -(offset + hip_swing) ]
        second_swing = [-x for x in first_swing]
        
        #LF, RM, LB
        #RB, LM, RF
        # recall: self.tripod1 = [self.left_front, self.right_middle, self.left_back]
        #         self.tripod2 = [self.right_front, self.left_middle, self.right_back]

        for x in xrange(repetitions + 1):

            for leg, angle in zip(self.tripod1, first_swing):
                leg.step(knee_end = raised, hip_end = angle)

            sleep(0.2)
         
            for leg, angle in zip(reversed(self.tripod2), first_swing):
                leg.step(hip_end = angle)

            for leg, angle in zip(self.tripod1, first_swing):
                leg.step(knee_end = floor, hip_end = angle)

            sleep(0.2)

            for leg, angle in zip(self.tripod2, second_swing):
                leg.step(knee_end = raised, hip_end = angle)

            sleep(0.2)
        
            for leg, angle in zip(reversed(self.tripod1), second_swing):
                leg.step(hip_end = angle)

            for leg, angle in zip(self.tripod2, second_swing):
                leg.step(knee_end = floor, hip_end = angle)

            sleep(0.2)
        
        

            

    

def calibrate_joint(joint, s, mn, mx, z):

    while True:
        for angle in [mn, z, mx, z]:
            joint.move(angle)
            sleep(s)

#hexy = Hexapod()
#calibrate_joint( hexy.right_back.ankle, s = 2, mn = -90, mx = 90, z = 0)

