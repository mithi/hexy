from Adafruit_PWM_Servo_Driver import PWM
from time import sleep
import threading 

# joint_key convention:
# R - right, L - left
# F - front, M - middle, B - back
# H - hip, K - knee, A - Ankle
# key : (channel, minimum_pulse_length, maximum_pulse_length)

joint_properties = {

    'LFH': (0, 248, 398), 'LFK': (1, 188, 476), 'LFA': (2, 131, 600),
    'RFH': (3, 275, 425), 'RFK': (4, 227, 507), 'RFA': (5, 160, 625),
    'LMH': (6, 312, 457), 'LMK': (7, 251, 531), 'LMA': (8, 138, 598),
    'RMH': (9, 240, 390), 'RMK': (10, 230, 514), 'RMA': (11, 150, 620),
    'LBH': (12, 315, 465), 'LBK': (13, 166, 466), 'LBA': (14, 140, 645),
    'RBH': (15, 265, 415), 'RBK': (16, 244, 544), 'RBA': (17, 150, 676),
    'N': (18, 105, 670)
}

driver1 = PWM(0x40)
driver2 = PWM(0x41)
driver1.setPWMFreq(60)
driver2.setPWMFreq(60)

def drive(ch, val):

    driver = driver1 if ch < 16 else driver2
    ch = ch if ch < 16 else ch - 16    

    driver.setPWM(ch, 0, val)

def constrain(val, min_val, max_val):

    if val < min_val: return min_val
    if val > max_val: return max_val
    return val

def remap(old_val, (old_min, old_max), (new_min, new_max)):

    new_diff = (new_max - new_min)*(old_val - old_min) / float((old_max - old_min))
    return int(round(new_diff)) + new_min 

class HexapodCore:

    def __init__(self):

        self.neck = Joint("neck", 'N')

        self.left_front = Leg('left front', 'LFH', 'LFK', 'LFA')
        self.right_front = Leg('right front', 'RFH', 'RFK', 'RFA')
        self.left_middle = Leg('left middle', 'LMH', 'LMK', 'LMA')
        self.right_middle = Leg('right middle', 'RMH', 'RMK', 'RMA')
        self.left_back = Leg('left back', 'LBH', 'LBK', 'LBA')
        self.right_back = Leg('right back', 'RBH', 'RBK', 'RBA')

        self.legs = [self.left_front, self.right_front,
                     self.left_middle, self.right_middle,
                     self.left_back, self.right_back]

        self.right_legs = [self.right_front, self.right_middle, self.right_back]
        self.left_legs = [self.left_front, self.left_middle, self.left_back]

        self.tripod1 = [self.left_front, self.right_middle, self.left_back]
        self.tripod2 = [self.right_front, self.left_middle, self.right_back]
        
        self.front_legs = [self.left_front, self.right_front]
        self.middle_legs = [self.left_middle, self.right_middle]
        self.back_legs = [self.left_back, self.right_back]

        self.hips = []
        self.knees = []
        self.ankles = []

        for leg in self.legs:
            self.hips.append(leg.hip)
            self.knees.append(leg.knee)
            self.ankles.append(leg.ankle)

    def off(self):

        for leg in self.legs:
            for joint in leg.joints:
                joint.off()

class Leg:

    def __init__(self, name, hip_key, knee_key, ankle_key):

        max_hip, max_knee, knee_leeway = 45, 50, 10
        self.hip = Joint("hip", hip_key, max_hip)
        self.knee = Joint("knee", knee_key, max_knee, leeway = knee_leeway)
        self.ankle = Joint("ankle", ankle_key)

        self.name = name
        self.joints = [self.hip, self.knee, self.ankle]

    def step(self, knee_end = None, hip_end = None):
        #knee_end < 0 means thigh is raised
        
        offset = 100

        if knee_end == None:
            knee_end = self.knee.angle
        if hip_end == None:
            hip_end = self.hip.angle

        self.move(hip_end, knee_end, knee_end - offset)

    def move(self, hip_end = 0, knee_end = 0, ankle_end = 0):

        self.hip.move(hip_end)
        self.knee.move(knee_end)
        self.ankle.move(ankle_end)
        
    def __repr__(self):
        return 'leg: ' + self.name

class Joint:

    def __init__(self, joint_type, jkey, maxx = 90, leeway = 0):

        self.joint_type, self.name =  joint_type, jkey
        self.channel, self.min_pulse, self.max_pulse = joint_properties[jkey]
        self.max, self.leeway = maxx, leeway
        self.off()

    def move(self, angle = 0):

        angle = constrain(angle, -(self.max + self.leeway), self.max + self.leeway)
        pulse = remap(angle, (-self.max, self.max), (self.min_pulse, self.max_pulse))

        #print repr(self), ':', 'pulse', pulse

        drive(self.channel, pulse)
        self.angle = angle

    def off(self):
        drive(self.channel, 0)
        self.angle = None

    def __repr__(self):
        return 'joint: ' + self.joint_type + ' : ' + self.name + ' angle: ' + str(self.angle)
 
