from robot_pro import HexapodPro
from time import sleep

class DancingHexapod(HexapodPro):

    def prepare(self, offset = 45, back_knee = 0, middle_knee = 50, front_knee = 60, raised = -30, s = 0.2):
        """ brings the back legs even further to the back and the middle legs to the front
            and then brings his further to the front """ 
        
        self.left_back.replant(raised, back_knee, offset, s)
        self.right_back.replant(raised, back_knee, -offset, s)
        self.left_middle.replant(raised, middle_knee, -offset, s)
        self.right_middle.replant(raised, middle_knee, offset, s)
        
        self.left_front.replant(raised, front_knee, -offset, s)
        self.right_front.replant(raised, front_knee, offset, s)

        self.neck.pose()

        sleep(s)
        
    def wave_right_arm_up(self):
    
        self.right_front.knee.pose(-60)
        self.right_front.ankle.pose(0)
        self.right_front.hip.pose(-45)
        hexy.neck.pose(-40)

    def wave_right_arm_down(self):
        self.right_front.knee.pose(50)
        self.right_front.ankle.pose(-50)
        self.right_front.hip.pose(45)
        hexy.neck.pose(0)
        
    def dip_body(self):
        
        self.left_middle.move(knee_angle = 50)
        self.right_middle.move(knee_angle = 50)
        self.left_back.move(knee_angle = -10)
        self.right_back.move(knee_angle = -10)

    def raise_body(self):
        
        self.left_middle.move(knee_angle = 70)
        self.right_middle.move(knee_angle = 70)
        self.left_back.move(knee_angle = 0)
        self.right_back.move(knee_angle = 0)

    def night_fever(self):

        self.prepare()
        
        for r in xrange(4):
            self.wave_right_arm_up()
            self.left_front.move(knee_angle = 40)
            self.dip_body()
            sleep(0.4)
            self.wave_right_arm_down()
            self.left_front.move(knee_angle = 60)
            self.raise_body()
            sleep(0.4)

    def arms_up_left(self):
        self.right_front.pose(knee_angle = -60, ankle_angle = -80, hip_angle = -45)
        self.left_front.pose(knee_angle = -60, ankle_angle = -80, hip_angle = -45)
        self.neck.pose(-45)

    def arms_up_right(self):
        self.right_front.pose(knee_angle = -60, ankle_angle = -80, hip_angle = 45)
        self.left_front.pose(knee_angle = -60, ankle_angle = -80, hip_angle = 45)
        self.neck.pose(45)

    def arms_down_center(self):
        self.right_front.pose(knee_angle = 30, ankle_angle = -60, hip_angle = 0)
        self.left_front.pose(knee_angle = 30, ankle_angle = -60, hip_angle = 0)
        self.neck.pose()

    def thriller_routine0(self):
        self.arms_down_center()
        self.raise_body()
        sleep(0.3)
        
    def thriller_routine1(self):
        self.thriller_routine0()
        self.arms_up_left()
        self.dip_body()
        sleep(0.3)
        
    def thriller_routine2(self):
        self.thriller_routine0()
        self.arms_up_right()
        self.dip_body()
        sleep(0.3)

    def thriller(self):
        
        self.prepare()

        for r in xrange(4):
            self.thriller_routine1()
            self.thriller_routine1()
            self.thriller_routine2()
            self.thriller_routine2()

            
hexy = DancingHexapod()

hexy.boot_up()
hexy.rest()

hexy.night_fever()
hexy.rest()

hexy.thriller()
hexy.rest()

hexy.shut_down()
    
