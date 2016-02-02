from robot_core import HexapodCore
from time import sleep

class Hexapod(HexapodCore):

    def walk(self, offset = 25 , hip_swing =  25, raised = -30, floor = 60, repetitions = 4, s = 0.15):
        #if hip_swing > 0, hexy moves forward else backward

        swing = [offset - hip_swing, hip_swing, -(offset + hip_swing)]
        reverse_swing = [-x for x in swing]
        
        for r in xrange(repetitions):
            self.stride(self.tripod1, self.tripod2[::-1], first_swing, raised, floor, s)
            self.stride(self.tripod2, self.tripod1[::-1], second_swing, raised, floor, s)

    def rotate(self, offset = 40, raised = -30, floor = 60, repetitions = 4, s = 0.15):

        for r in xrange(repetitions):
            #replant tripod2 with an offset
            self.uniform_tripod_step(self.tripod2, None, raised, s)
            self.uniform_tripod_step(self.tripod2, offset, floor, s)

            #raise tripod1 
            self.uniform_tripod_step(self.tripod1, None, raised, s)

            #swing tripod2's hips to an -offset
            self.uniform_tripod_step(self.tripod2, -offset, None, s) 

            #lower tripod1   
            self.uniform_tripod_step(self.tripod1, offset, floor, s)
        
    def curl_up(self, s = 0.2, die = False):

        for leg in self.legs:
            leg.hip.move(0)
            leg.knee.move(-(leg.knee.max + leg.knee.leeway))
            leg.ankle.move(leg.ankle.max)

        sleep(s)

        if die: self.off()

    def lie_flat(self, s = 0.15):
        
        for leg in self.legs:
            leg.move()
            
        sleep(s)

    def lie_down(self, maxx = 50, step = 4, s = 0.15):
        
        for angle in xrange(maxx, -(maxx + 1), -step):
            self.step_all(angle)

        sleep(s)

    def get_up(self, maxx = 50, step = 4, s = 0.15):

        for angle in xrange(-maxx, maxx + 1, step):
            self.step_all(angle)

        sleep(s)
        
    def twist_hip(self, angle = 0, s = 0.1):

        for hip in self.hips:
            hip.move(angle)

        sleep(s)

    def step_all(self, angle):
        
        for leg in self.legs:
            leg.step(angle)

    def uniform_tripod_step(self, tripod, hip_angle, knee_angle, s = 0):
        
        for leg in tripod:
            leg.step(knee_angle, hip_angle)

        sleep(s)

    def tripod_step(self, tripod, hip_swings, knee_angle, s = 0):
        
        for leg, hip_angle in zip(tripod, hip_swings):
            leg.step(knee_angle, hip_angle)

        sleep(s)
            
    def stride(self, tripod_a, tripod_b, swing, raised, floor, s):

        self.tripod_step(tripod_a, [None, None, None], raised)
        sleep(s)
        
        self.tripod_step(tripod_b, swing, None)
        self.tripod_step(tripod_a, swing, floor)
        sleep(s)
