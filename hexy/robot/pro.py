from hexapod import Hexapod
from time import sleep

class HexapodPro(Hexapod):

    def shake_head(self, maxx = 60, repetitions = 5, t = 0.2):

        for r in xrange(repetitions):
            self.look(maxx, t)
            self.look(-maxx, t)
        
        self.look()

    def point(self, t = 0.75):
        
        self.left_front.hip.pose(-45)
        self.left_front.knee.pose(-50)
        self.left_front.ankle.pose(-55)

        sleep(t)

    def wave(self, repetitions = 5, t = 0.2):
        
        self.left_front.ankle.pose()
        self.left_front.knee.pose(-50)
        
        for r in xrange(repetitions):
            self.left_front.hip.pose(-45)
            sleep(t)
            self.left_front.hip.pose(45)
            sleep(t)

    def dance_twist(self, maxx = 45, step = 5, repetitions = 3, t = 0.01):

        self.squat(60, t)

        for r in xrange(repetitions):
            
            for angle in xrange(-maxx, maxx, step):
                self.twist_hip(angle, t)
            
            for angle in xrange(maxx, -maxx, -step):
                self.twist_hip(angle, t)

        self.twist_hip()
        self.squat(60, t)


    def lean_back(self, offset = 45, back_knee = 0, middle_knee = 40, raised = -30, t = 0.2):
        """ brings the back legs even further to the back and the middle legs to the front
            and then brings his front legs up in the air """ 
        
        self.left_back.replant(raised, back_knee, offset, t)
        self.right_back.replant(raised, back_knee, -offset, t)
        self.left_middle.replant(raised, middle_knee, -offset, t)
        self.right_middle.replant(raised, middle_knee, offset, t)
        
        self.left_front.pose(-offset, 0, 0)
        self.right_front.pose(offset, 0, 0)

        sleep(t)

    def type_stuff(self, up = -40, down = 40, repetitions = 5, t = 0.2):

        self.lean_back()

        for r in xrange(repetitions):

            self.left_front.knee.pose(up)
            self.right_front.knee.pose(down)
            sleep(t)

            self.right_front.knee.pose(up)
            self.left_front.knee.pose(down)
            sleep(t)
        
        sleep(t)

    def tilt_left_and_right(self, raised = 60, floor = 20, repetitions = 5, t = 0.15):
        
        for r in xrange(repetitions):
            self.tilt_side(left_angle = floor, right_angle = raised)
            self.tilt_side(left_angle = raised, right_angle = floor)

        self.squat(raised, t)

    def tilt_front_and_back(self, up = 60, mid = 40, down = 20, repetitions = 5, t = 0.15):
        
        for r in xrange(repetitions):
            self.tilt(up, mid, down)
            self.tilt(down, mid, up)

        self.squat(up, t)
    
    def dance_tilt(self, raised = 60, mid = 40, floor = 20, repetitions = 3, t = 0.15):

        for r in xrange(repetitions):
            
            self.tilt(floor, mid, raised, t) # front
            self.tilt_side(raised, floor, t) # right
            self.tilt(raised, mid, floor, t) # back
            self.tilt_side(floor, raised, t) # left

        self.squat(raised, t)

    def rock_body(self,  offset = 45, floor = 50, repetitions = 7):

        for r in xrange(repetitions):
            self.uniform_move(self.left_legs, offset, floor, 0)
            self.uniform_move(self.right_legs, -offset, floor, 0.2)
            self.uniform_move(self.left_legs, -offset, floor, 0)
            self.uniform_move(self.right_legs, offset, floor, 0.2)
