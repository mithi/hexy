from core import HexapodCore
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

    def curl_up(self, die = False, t = 0.2):

        for leg in self.legs:
            leg.pose(hip_angle = 0, 
                     knee_angle = -(leg.knee.max + leg.knee.leeway), 
                     ankle_angle = leg.ankle.max)

        sleep(t)

        if die: self.off()
        
    def lie_flat(self, t = 0.15):
        
        for leg in self.legs:
            leg.pose()
            
        sleep(t)

    def lie_down(self, maxx = 50, step = 4, t = 0.15):
        
        for angle in xrange(maxx, -(maxx + 1), -step):
            self.squat(angle)

        sleep(t)

    def get_up(self, maxx = 70, step = 4):

        for angle in xrange(-maxx, maxx + 1, step):
            self.squat(angle)

        self.default()

    def look(self, angle = 0, t = 0.05):
        self.neck.pose(angle)
        sleep(t)

    def twist_hip(self, angle = 0, t = 0.1):

        for hip in self.hips:
            hip.pose(angle)

        sleep(t)
        
    def squat(self, angle, t = 0):

        for leg in self.legs:
            leg.move(knee_angle = angle)

        sleep(t)

    def walk(self, offset = 25 , swing =  25, raised = -30, floor = 50, repetitions = 4, t = 0.2):
        """ if swing > 0, hexy moves forward else backward """
        
        swings = [offset - swing, swing, -(offset + swing)]
        reverse_swings = [-x for x in swings]
        
        for r in xrange(repetitions):
            self.stride(self.tripod1, self.tripod2, swings, raised, floor, t)
            self.stride(self.tripod2, self.tripod1, reverse_swings, raised, floor, t)

    def rotate(self, offset = 40, raised = -30, floor = 50, repetitions = 5, t = 0.2):
        """ if offset > 0, hexy rotates left, else right """
       
        for r in xrange(repetitions):
            
            #replant tripod2 with an offset
            self.uniform_move(self.tripod2, None, raised, t)
            self.uniform_move(self.tripod2, offset, floor, t)

            #raise tripod1
            self.uniform_move(self.tripod1, -offset, raised) 
            
            #swing tripod2's hips to an -offset 
            self.uniform_move(self.tripod2, -offset, None, t)
            
            #lower tripod1
            self.uniform_move(self.tripod1, 0, floor, t)

            
    def stride(self, first_tripod, second_tripod, swing, raised, floor, t):
        """ first_tripod's legs replant to propel towards a direction while
            second_tripod's legs retrack by swinging to the opposite direction """

        self.simultaneous_move(first_tripod, knee_angle = raised)
        sleep(t)
        
        self.simultaneous_move(second_tripod, swing[::-1])
        self.simultaneous_move(first_tripod, swing, floor)
        sleep(t)

    def tilt_side(self, left_angle = 50, right_angle = 0, t = 0.2):
        """ if left_angle > right_angle, left side is higher than right side """
        
        self.uniform_move(legs = self.left_legs, knee_angle = left_angle)
        self.uniform_move(legs = self.right_legs, knee_angle = right_angle)
        sleep(t)

    def tilt(self, front_angle = 50, middle_angle = 25, back_angle = 0, t = 0.2):
        """ if front_angle > middle_angle > back_angle hexy's front is higher than his back """

        self.right_front.move(knee_angle = front_angle)
        self.left_front.move(knee_angle = front_angle)

        self.right_middle.move(knee_angle = middle_angle)
        self.left_middle.move(knee_angle = middle_angle)

        self.right_back.move(knee_angle = back_angle)
        self.left_back.move(knee_angle = back_angle)

        sleep(t)

    def default(self, offset = 45, floor = 60, raised = -30,  t = 0.2):
        """ Hexy's default pose, offset > 0 brings the front and back legs to the side """ 
        
        swings = [offset, 0, -offset]

        self.look()
        self.squat(floor, t)
        
        self.simultaneous_move(self.tripod1, swings, raised, t)
        self.simultaneous_move(self.tripod1, swings, floor, t)
        self.simultaneous_move(self.tripod2, swings[::-1], raised, t)
        self.simultaneous_move(self.tripod2, swings[::-1], floor, t)

    def uniform_move(self, legs, hip_angle = None, knee_angle = None, t = 0):
        """ moves all legs with hip_angle, knee_angle """
        
        for leg in legs:
            leg.move(knee_angle, hip_angle)

        sleep(t)

    def simultaneous_move(self, legs, swings = [None, None, None], knee_angle = None, t = 0):
        """ moves all legs with knee_angle to the respective hip angles at 'swing' """
        
        for leg, hip_angle in zip(legs, swings):
            leg.move(knee_angle, hip_angle)

        sleep(t)

