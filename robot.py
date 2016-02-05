from robot_core import HexapodCore
from time import sleep

class Hexapod(HexapodCore):

    def boot_up(self):
        
        self.lie_down()
        self.curl_up()
        self.lie_flat()
        self.get_up()

    def shut_down(self):

        self.twist_hip()
        self.lie_down()
        self.lie_flat()
        self.curl_up()
        self.off()

    def rest(self, s = 0.5):
        
        self.pose_attention()
        sleep(s)
        self.off()
        sleep(4*s)
        self.pose_attention()
        sleep(s)

    def walk(self, offset = 25 , swing =  25, raised = -30, floor = 50, repetitions = 4, s = 0.2):
        """ if hip_swing > 0, hexy moves forward else backward
            ideal offset is a positive number (25)"""
        

        swings = [offset - swing, swing, -(offset + swing)]
        reverse_swings = [-x for x in swings]
        
        for r in xrange(repetitions):
            self.stride(self.tripod1, self.tripod2[::-1], swings, raised, floor, s)
            self.stride(self.tripod2, self.tripod1[::-1], reverse_swings, raised, floor, s)

        self.pose_attention()

    def rotate(self, offset = 40, raised = -30, floor = 50, repetitions = 5, s = 0.2):
        """ if offset > 0, hexy rotates left, else right """
       
        for r in xrange(repetitions):
            
            #replant tripod2 with an offset
            self.uniform_step(self.tripod2, None, raised, s)
            self.uniform_step(self.tripod2, offset, floor, s)

            #raise tripod1 
            self.uniform_step(self.tripod1, -offset, raised)

            #swing tripod2's hips to an -offset
            self.uniform_step(self.tripod2, -offset, None, s) 

            #lower tripod1   
            self.uniform_step(self.tripod1, 0, floor, s)

    def tilt_left_and_right(self, floor = 50, raised = 0, repetitions = 5):
        
        for r in xrange(repetitions):
            self.tilt_side(left_angle = floor, right_angle = raised)
            self.tilt_side(left_angle = raised, right_angle = floor)

    def tilt_front_and_back(self, up = 50, mid = 25, down = 0, repetitions = 5):
        
        for r in xrange(repetitions):
            self.tilt(up, mid, down)
            self.tilt(down, mid, up)
    
    def dance_tilt_ccw(self, raised = 50, mid = 25, floor = 0, repetitions = 3, s = 0.15):

        for r in xrange(repetitions):
            
            self.tilt(floor, mid, raised, s) # front
            self.tilt_side(floor, raised, s) # left
            self.tilt(raised, mid, floor, s) # back
            self.tilt_side(raised, floor, s) # right

    def dance_tilt_cw(self, raised = 50, mid = 25, floor = 0, repetitions = 3, s = 0.15):

        for r in xrange(repetitions):
            
            self.tilt(floor, mid, raised, s) # front
            self.tilt_side(raised, floor, s) # right
            self.tilt(raised, mid, floor, s) # back
            self.tilt_side(floor, raised, s) # left 

    def dance_tilt(self, repetitions = 2):

        for r in xrange(repetitions):
           self.dance_tilt_cw()
           self.dance_tilt_ccw()
    
    def tilt_side(self, left_angle = 50, right_angle = 0, s = 0.2):
        """ if left_angle > right_angle, left side is higher than right side """
            
        for leg in self.left_legs:
            leg.step(knee_end = left_angle)

        for leg in self.right_legs:
            leg.step(knee_end = right_angle)

        sleep(s)

    def tilt(self, front_angle = 50, middle_angle = 25, back_angle = 0, s = 0.2):
        """ if front_angle > middle_angle > back_angle hexy's front is higher than his back """

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

    def get_up(self, maxx = 70, step = 4, s = 0.15):

        for angle in xrange(-maxx, maxx + 1, step):
            self.step_all(angle)

        self.pose_attention()
        sleep(s)

    def pose_attention(self, offset = 45, floor = 50, raised = -30,  s = 0.2):
        """ default pose of the hexapod, offset > 0 brings the front and back legs to the side """ 
          
        swings = [offset, 0, -offset]
 
        self.swing_step(self.tripod1, swings, raised, s) 
        self.swing_step(self.tripod1, swings, floor, s)
        self.swing_step(self.tripod2[::-1], swings, raised, s)
        self.swing_step(self.tripod2[::-1], swings, floor, s)
            
    def shake_head(self, maxx = 60, repetitions = 5, s = 0.2):

        for r in xrange(repetitions):
            self.neck.move(maxx)
            sleep(s)
            self.neck.move(-maxx)
            sleep(s)

        self.neck.move()

    def point(self, s = 0.15):
        
        self.left_front.hip.move(-45)
        self.left_front.knee.move(-50)
        self.left_front.ankle.move(-55)

        sleep(s)

    def wave(self, repetitions = 5, s = 0.2):
        self.left_front.ankle.move()
        self.left_front.knee.move(-50)
        
        for r in xrange(repetitions):
            self.left_front.hip.move(-45)
            sleep(s)
            self.left_front.hip.move(45)
            sleep(s)
        

    def lean_back(self, offset = 45, back_knee = 0, middle_knee = 40, raised = -30, s = 0.2):
        """ brings the back legs even further to the back and the middle legs to the front
            and then brings his front legs up in the air """ 
        
        self.left_back.replant(raised, back_knee, offset, s)
        self.right_back.replant(raised, back_knee, -offset, s)
        self.left_middle.replant(raised, middle_knee, -offset, s)
        self.right_middle.replant(raised, middle_knee, offset, s)
        
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

    def twist_hip_slowly(self, maxx = 45, step = 5, repetitions = 3, s = 0.01):

        for r in xrange(repetitions):
            for angle in xrange(-maxx, maxx, step):
                self.twist_hip(angle, s)
            for angle in xrange(maxx, -maxx, -step):
                self.twist_hip(angle, s)

    def twist_hip(self, angle = 0, s = 0.1):

        for hip in self.hips:
            hip.move(angle)

        sleep(s)
        
    def step_all(self, angle):
        
        for leg in self.legs:
            leg.step(angle)

    def uniform_step(self, legs, hip_angle, knee_angle, s = 0):
        """ steps all legs in list 'legs' using parameters hip_angle, knee_angle """
        
        for leg in legs:
            leg.step(knee_angle, hip_angle)

        sleep(s)

    def swing_step(self, legs, swings, knee_angle = None, s = 0):
        """ moves all legs in list 'legs' tripod to a uniform knee_angle and
            to the respective hip_angles specified at list 'swing' """
        
        for leg, hip_angle in zip(legs, swings):
            leg.step(knee_angle, hip_angle)

        sleep(s)
            
    def stride(self, tripod_a, tripod_b, swing, raised, floor, s):
        """ replants all legs in list 'tripod_a' to the respective hip_angles specified
            at list 'swing' by raising at a knee_angle of 'raised' to a knee_angle of 'floor'
            while swinging all legs list 'tripod_b' to the same hip angles of 'tripod_a'"""

        self.swing_step(tripod_a, [None, None, None], raised)
        sleep(s)
        
        self.swing_step(tripod_b, swing, None)
        self.swing_step(tripod_a, swing, floor)
        sleep(s)
