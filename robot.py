from robot_core import HexapodCore
from time import sleep

class Hexapod(HexapodCore):

    def walk(self, offset = 25 , hip_swing =  25, raised = -30, floor = 60, repetitions = 4, s = 0.2):
        #if hip_swing > 0, hexy moves forward else backward

        swing = [offset - hip_swing, hip_swing, -(offset + hip_swing)]
        reverse_swing = [-x for x in swing]
        
        for r in xrange(repetitions):
            self.stride(self.tripod1, self.tripod2[::-1], swing, raised, floor, s)
            self.stride(self.tripod2, self.tripod1[::-1], reverse_swing, raised, floor, s)

        self.pose_attention()

    def rotate(self, offset = 40, raised = -30, floor = 60, repetitions = 4, s = 0.2):
        
        for r in xrange(repetitions):
            #replant tripod2 with an offset
            self.uniform_tripod_step(self.tripod2, None, raised, s)
            self.uniform_tripod_step(self.tripod2, offset, floor, s)

            #raise tripod1 
            self.uniform_tripod_step(self.tripod1, None, raised)

            #swing tripod2's hips to an -offset
            self.uniform_tripod_step(self.tripod2, -offset, None, s) 

            #lower tripod1   
            self.uniform_tripod_step(self.tripod1, offset, floor, s)       

    def tilt_side(self, left_angle = 50, right_angle = 0, offset = 45, s = 0.1):
        # if left_angle > right_angle, left side will be higher than right side

        self.prepare(offset)
            
        for leg in self.left_legs:
            leg.step(knee_end = left_angle)

        for leg in self.right_legs:
            leg.step(knee_end = right_angle)

        sleep(s)

    def tilt(self, front_angle = 50, middle_angle = 25, back_angle = 0, offset = 45, s = 0.1):

        self.prepare(offset)

        self.right_front.step(knee_end = front_angle)
        self.left_front.step(knee_end = front_angle)

        self.right_middle.step(knee_end = middle_angle)
        self.left_middle.step(knee_end = middle_angle)

        self.right_back.step(knee_end = back_angle)
        self.left_back.step(knee_end = back_angle)

        sleep(s)

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

    def pose_attention(self, offset = 45, raised = -30, floor = 50, s = 0.2):

        swing = [-offset, 0, offset]

        self.stride(self.tripod1, self.tripod2[::-1], swing, raised, floor, s)
        self.stride(self.tripod2, self.tripod1[::-1], swing, raised, floor, s)

    def shake_head(self, repetitions = 5, maxx = 60,  s = 0.2):

        for r in xrange(5):
            self.neck.move(maxx)
            sleep(s)
            self.neck.move(-maxx)
            sleep(s)

        self.neck.move()

    def point(self, s = 0.2):
        
        self.left_front.hip.move(-45)
        self.left_front.knee.move(-50)
        self.left_front.ankle.move(-55)

        sleep(s)

    def lean_back(self, offset = 45, back_knee = 0, middle_knee = 25, s = 0.3):

        self.left_back.step(back_knee, offset)
        self.right_back.step(back_knee, -offset)

        self.left_middle.step(middle_knee, offset)
        self.right_middle.step(middle_knee, -offset)
        
        self.left_front.move(-offset, 0, 0)
        self.right_front.move(offset, 0, 0)

        sleep(s)

    def type_stuff(self, up = -40, down = 40, repetitions = 5, s = 0.2):

        self.lean_back()

        for r in xrange(repetitions):

            self.left_front.knee.move(up)
            self.right_front.knee.move(down)
            sleep(s)

            self.right_front.knee.move(up)
            self.left_front.knee.move(down)
            sleep(s)

    def twist_hip(self, angle = 0, s = 0.1):

        for hip in self.hips:
            hip.move(angle)

        sleep(s)

    def prepare(self, offset):
        
        hip_angles = [offset, 0, -offset]

        self.tripod_step(self.tripod1, hip_angles)        
        self.tripod_step(self.tripod2[::-1], hip_angles)
        
    def step_all(self, angle):
        
        for leg in self.legs:
            leg.step(angle)

    def uniform_tripod_step(self, tripod, hip_angle, knee_angle, s = 0):
        
        for leg in tripod:
            leg.step(knee_angle, hip_angle)

        sleep(s)

    def tripod_step(self, tripod, hip_swings, knee_angle = None, s = 0):
        
        for leg, hip_angle in zip(tripod, hip_swings):
            leg.step(knee_angle, hip_angle)

        sleep(s)
            
    def stride(self, tripod_a, tripod_b, swing, raised, floor, s):

        self.tripod_step(tripod_a, [None, None, None], raised)
        sleep(s)
        
        self.tripod_step(tripod_b, swing,)
        self.tripod_step(tripod_a, swing, floor)
        sleep(s)
