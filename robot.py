from core_robot import HexapodCore
from time import sleep

class Hexapod(HexapodCore):

    def curl_up(self, s = 0.2, die = False):

        for leg in self.legs:
            leg.hip.move(0)
            leg.knee.move(-70)
            leg.ankle.move(leg.ankle.max)

        sleep(s)

        if die: self.off()
        

    def lie_flat(self, s = 0.15):
        
        for leg in self.legs:
            leg.move()
            
        sleep(s)

    def step_all(self, angle):
        for leg in self.legs:
            leg.step(angle)


    def lie_down(self, maxx = 50, step = 4, s = 0.15):
        
        for angle in xrange(maxx, -(maxx + 1), -step):
            self.step_all(angle)

        sleep(s)
            
        
    def get_up(self, maxx = 50, step = 4, s = 0.15):

        for angle in xrange(-maxx, maxx + 1, step):
            self.step_all(angle)

        sleep(s)

    def twist_hip(self, angle = 0, s = 0.2):

        for hip in self.hips:
            hip.move(angle)

        sleep(s)

    def tripod_step(self, tripod, hip_swings, knee_angle):
        
        for leg, hip_angle in zip(tripod, hip_swings):
            leg.step(knee_end = knee_angle, hip_end = hip_angle)

    def stride(self, tripod_a, tripod_b, swing, raised, floor, s):

        self.tripod_step(tripod_a, swing, raised)
        sleep(s)
        
        self.tripod_step(tripod_b, swing, None)
        self.tripod_step(tripod_a, swing, floor)
        sleep(s)

    def move(self, repetitions, first_swing, second_swing, raised, floor, s):
        
        for x in xrange(repetitions):
            self.stride(self.tripod1, self.tripod2, first_swing, raised, floor, s)
            self.stride(self.tripod2, self.tripod1, second_swing, raised, floor, s)

    def walk_forward(self, offset = 25 , hip_swing =  20, raised = -30, floor = 70, repetitions = 5, s = 0.2):

        first_swing = [offset - hip_swing, hip_swing, -(offset + hip_swing)]
        second_swing = [offset + hip_swing, -hip_swing, -(offset - hip_swing)]

        self.move(repetitions, first_swing, second_swing, raised, floor, s)            
      
            
def calibrate_joint(joint, s, mn, mx, z):

    while True:
        for angle in [mn, z, mx, z]:
            joint.move(angle)
            sleep(s)

#hexy = Hexapod()
#calibrate_joint( hexy.right_back.ankle, s = 2, mn = -90, mx = 90, z = 0)

