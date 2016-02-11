from robot_core import HexapodCore
from time import sleep

class Hexapod(HexapodCore):

    def boot_up(self):
  
        self.look()
        self.lie_down()
        self.curl_up()
        self.lie_flat()
        self.get_up()

    def shut_down(self):

        self.look()
        self.lie_down()
        self.lie_flat()
        self.curl_up(die = True)

    def curl_up(self, s = 0.2, die = False):

        for leg in self.legs:
            leg.pose(hip_angle = 0, 
                     knee_angle = -(leg.knee.max + leg.knee.leeway), 
                     ankle_angle = leg.ankle.max)

        sleep(s)

        if die: self.off()
        
    def lie_flat(self, s = 0.15):
        
        for leg in self.legs:
            leg.pose()
            
        sleep(s)

    def lie_down(self, maxx = 50, step = 4, s = 0.15):
        
        for angle in xrange(maxx, -(maxx + 1), -step):
            self.squat(angle)

        sleep(s)

    def get_up(self, maxx = 70, step = 4, s = 0.15):

        for angle in xrange(-maxx, maxx + 1, step):
            self.squat(angle)

        self.pose_default()

    def rest(self, knee_angle = 60, s = 0.3):
        
        self.squat(knee_angle, s)        
        self.off()
        sleep(s)
        self.squat(knee_angle, s)    
        self.pose_default()

    def look(self, angle = 0, s = 0.05):
        self.neck.pose(angle)
        sleep(s)

    def twist_hip(self, angle = 0, s = 0.1):

        for hip in self.hips:
            hip.pose(angle)

        sleep(s)
        
    def squat(self, knee_angle, s = 0):
        
        for leg in self.legs:
            leg.move(knee_angle)

        sleep(s)

    def walk(self, offset = 25 , swing =  25, raised = -30, floor = 50, repetitions = 4, s = 0.2):
        """ if swing > 0, hexy moves forward else backward, preferrably offset > 0 """
        
        swings = [offset - swing, swing, -(offset + swing)]
        reverse_swings = [-x for x in swings]
        
        for r in xrange(repetitions):
            self.stride(self.tripod1, self.tripod2, swings, raised, floor, s)
            self.stride(self.tripod2, self.tripod1, reverse_swings, raised, floor, s)

    def rotate(self, offset = 40, raised = -30, floor = 50, repetitions = 5, s = 0.2):
        """ if offset > 0, hexy rotates left, else right """
       
        for r in xrange(repetitions):
            
            #replant tripod2 with an offset
            self.uniform_move(self.tripod2, None, raised, s)
            self.uniform_move(self.tripod2, offset, floor, s)

            #raise tripod1
            self.uniform_move(self.tripod1, -offset, raised) 
            
            #swing tripod2's hips to an -offset 
            self.uniform_move(self.tripod2, -offset, None, s) 
            
            #lower tripod1
            self.uniform_move(self.tripod1, 0, floor, s)

    def pose_default(self, offset = 45, floor = 50, raised = -30,  s = 0.2):
        """ default pose of the hexapod, offset > 0 brings the front and back legs to the side """ 
          
        swings = [offset, 0, -offset]
        self.look()
        self.simultaneous_move(self.tripod1, swings, raised, s) 
        self.simultaneous_move(self.tripod1, swings, floor, s)
        self.simultaneous_move(self.tripod2[::-1], swings, raised, s)
        self.simultaneous_move(self.tripod2[::-1], swings, floor, s)

    def uniform_move(self, legs, hip_angle = None, knee_angle = None, s = 0):
        """ moves all legs in 'legs' using parameters hip_angle, knee_angle """
        
        for leg in legs:
            leg.move(knee_angle, hip_angle)

        sleep(s)

    def simultaneous_move(self, legs, swings = [None, None, None], knee_angle = None, s = 0):
        """ moves all legs to the respective hip angles specified at 'swing' at the same 'knee_angle' """
        
        for leg, hip_angle in zip(legs, swings):
            leg.move(knee_angle, hip_angle)

        sleep(s)
            
    def stride(self, first_tripod, second_tripod, swing, raised, floor, s):
        """ legs at first_tripod replants to propel towards a direction while
            legs at second_tripod retracks by swinging to the opposite direction """

        self.simultaneous_move(first_tripod, knee_angle = raised)
        sleep(s)
        
        self.simultaneous_move(second_tripod, swing[::-1])
        self.simultaneous_move(first_tripod, swing, floor)
        sleep(s)

    def tilt_side(self, left_angle = 50, right_angle = 0, s = 0.2):
        """ if left_angle > right_angle, left side is higher than right side """
        
        self.uniform_move(legs = left_legs, knee_angle = left_angle)
        self.uniform_move(legs = right_legs, knee_angle = right_angle)
        sleep(s)

    def tilt(self, front_angle = 50, middle_angle = 25, back_angle = 0, s = 0.2):
        """ if front_angle > middle_angle > back_angle hexy's front is higher than his back """

        self.right_front.move(knee_angle = front_angle)
        self.left_front.move(knee_angle = front_angle)

        self.right_middle.move(knee_angle = middle_angle)
        self.left_middle.move(knee_angle = middle_angle)

        self.right_back.move(knee_angle = back_angle)
        self.left_back.move(knee_angle = back_angle)

        sleep(s)

