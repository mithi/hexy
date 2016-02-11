from robot import Hexapod
from time import sleep

class HexapodPro(Hexapod):

    def shake_head(self, maxx = 60, repetitions = 5, s = 0.2):

        for r in xrange(repetitions):
            self.look(maxx, s)
            self.look(-maxx, s)
        
        self.look()

    def point(self, s = 0.15):
        
        self.left_front.hip.pose(-45)
        self.left_front.knee.pose(-50)
        self.left_front.ankle.pose(-55)

        sleep(s)

    def wave(self, repetitions = 5, s = 0.2):
        
        self.left_front.ankle.pose()
        self.left_front.knee.pose(-50)
        
        for r in xrange(repetitions):
            self.left_front.hip.pose(-45)
            sleep(s)
            self.left_front.hip.pose(45)
            sleep(s)

    def dance_twist(self, maxx = 45, step = 5, repetitions = 3, s = 0.01):

        self.squat(raised, s)

        for r in xrange(repetitions):
            
            for angle in xrange(-maxx, maxx, step):
                self.twist_hip(angle, s)
            
            for angle in xrange(maxx, -maxx, -step):
                self.twist_hip(angle, s)

        self.twist_hip()
        self.squat(raised, s)


    def lean_back(self, offset = 45, back_knee = 0, middle_knee = 40, raised = -30, s = 0.2):
        """ brings the back legs even further to the back and the middle legs to the front
            and then brings his front legs up in the air """ 
        
        self.left_back.replant(raised, back_knee, offset, s)
        self.right_back.replant(raised, back_knee, -offset, s)
        self.left_middle.replant(raised, middle_knee, -offset, s)
        self.right_middle.replant(raised, middle_knee, offset, s)
        
        self.left_front.pose(-offset, 0, 0)
        self.right_front.pose(offset, 0, 0)

        sleep(s)

    def type_stuff(self, up = -40, down = 40, repetitions = 5, s = 0.2):

        self.lean_back()

        for r in xrange(repetitions):

            self.left_front.knee.pose(up)
            self.right_front.knee.pose(down)
            sleep(s)

            self.right_front.knee.pose(up)
            self.left_front.knee.pose(down)
            sleep(s)
        
        sleep(s)

    def tilt_left_and_right(self, raised = 60, floor = 0, repetitions = 5, s = 0.15):
        
        for r in xrange(repetitions):
            self.tilt_side(left_angle = floor, right_angle = raised)
            self.tilt_side(left_angle = raised, right_angle = floor)

        self.squat(raised, s)

    def tilt_front_and_back(self, up = 60, mid = 25, down = 0, repetitions = 5, s = 0.15):
        
        for r in xrange(repetitions):
            self.tilt(up, mid, down)
            self.tilt(down, mid, up)

        self.squat(raised, s)
    
    def dance_tilt_ccw(self, raised = 60, mid = 25, floor = 0, repetitions = 3, s = 0.15):

        for r in xrange(repetitions):
            
            self.tilt(floor, mid, raised, s) # front
            self.tilt_side(floor, raised, s) # left
            self.tilt(raised, mid, floor, s) # back
            self.tilt_side(raised, floor, s) # right

        self.squat(raised, s)

    def dance_tilt_cw(self, raised = 50, mid = 25, floor = 0, repetitions = 3, s = 0.15):

        for r in xrange(repetitions):
            
            self.tilt(floor, mid, raised, s) # front
            self.tilt_side(raised, floor, s) # right
            self.tilt(raised, mid, floor, s) # back
            self.tilt_side(floor, raised, s) # left

        self.squat(raised, s)

    def dance_tilt(self, repetitions = 2, s = 0.15):

        for r in xrange(repetitions):
           self.dance_tilt_cw(repetitions = 1)
           self.dance_tilt_ccw(repetitions = 1)

        self.squat(raised, s = 0.15)
        
    def rock_body(self,  offset = 45, floor = 50, repetitions = 7):

        for r in xrange(repetitions):
            self.uniform_move(self.left_legs, offset, floor, 0)
            self.uniform_move(self.right_legs, -offset, floor, 0.2)
            self.uniform_move(self.left_legs, -offset, floor, 0)
            self.uniform_move(self.right_legs, offset, floor, 0.2)
            