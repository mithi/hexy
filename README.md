[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/minimithi)

# TABLE OF CONTENTS
- Links
- Stuff to Buy and Assemble
- - Electronic Hardware Stuff
- - Frame 
- - Connect Stuff and Calibrate Servos
- Forks by Others
- Configuration and Calibration 
- Sample Usage

#  LINKS
- [Hexy Documentation](http://hexyrobot.wordpress.com)
- [Hexy Transcript](https://medium.com/@mithi/a-raspberry-pi-hexy-transcript-62533c69a566)

# STUFF TO BUY AND ASSEMBLE

## Electronic Hardware stuff 
I bought a bunch of stuff, here are the most important stuff:
- [Two Adafruit 16-channel PWM servo drivers](https://learn.adafruit.com/16-channel-pwm-servo-driver)
- [A Raspberry Pi Zero](https://www.adafruit.com/product/3400)
- [Nineteen DFRobot 9g metal gear servos (1.8kg torque)](https://www.dfrobot.com/product-1338.html)
- [5V, 10A power supply](https://www.adafruit.com/product/658)
- [All other stuff outlined here](https://hexyrobot.wordpress.com/2016/02/08/hexy-modifications/) 

## Frame
The screws and nuts are the 3M ones you can buy from your local hardware store. You can lazer cut or 3D print 
Arcbotic's Hexapod frame as they have open-sources the files in DXF and STL format. I used a 5mm acrylic sheet. 
- [Arcbotics Frame](https://github.com/arcbotics/hexy)
- [Arcbotics Frame Build Instructions](http://arcbotics.com/products/hexy/start/)

## Connect Stuff and Calibrate Servos
Adafruit has good tutorials for how to wire the drivers and all with the Arduino and Raspberry Pi. 
- [Servo Driver with Arduino](https://learn.adafruit.com/16-channel-pwm-servo-driver?view=all)
- [Servo Driver Hat with Raspberry Pi](https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield?view=all)
- The large Raspberry Pi 2B and 3B has the same 40-pin configuration as the Raspberry Pi Zero, you just follow how to wire the I2C pins there. 
- These tutorials are also good starting point to calibrate the minimum and maximum pulses of each of your servo which you'd have to do. 

# CHECKOUT FORKS BY OTHERS

@robottwo has implemented a nice gui and config file which I haven't merged (or let alone tested), 
you might be interested cloning that instead: 

- [ROBOTTWO'S FORK](https://github.com/robottwo/hexy/tree/config)
> You may have your servo controllers on different addresses, or your servos plugged into different ports. You will also have to calibrate the min and max range of each of your servos, since these settings vary from servo to servo.
These settings are all stored in the hexy.cfg file. To help with this task, there is a GUI program scripts/detect_controllers.py. - ROBOTTWO

# CONFIGURATION AND CALIBRATION

You should take a look at the base file here as it is implemented in a pretty straightforward manner:
- [BASE FILE - CORE.PY](https://github.com/mithi/hexy/blob/master/hexy/robot/core.py)

You may need to edit `lines 4 to 22` of this file (and a bunch of other lines) depending on the configuration of your Hexapod and if you are using a different frame or if you are using different I2C addresses.  

```
""" joint_key convention:
    R - right, L - left
    F - front, M - middle, B - back
    H - hip, K - knee, A - Ankle
    key : (channel, minimum_pulse_length, maximum_pulse_length) """

joint_properties = {

    'LFH': (0, 248, 398), 'LFK': (1, 188, 476), 'LFA': (2, 131, 600),
    'RFH': (3, 275, 425), 'RFK': (4, 227, 507), 'RFA': (5, 160, 625),
    'LMH': (6, 312, 457), 'LMK': (7, 251, 531), 'LMA': (8, 138, 598),
    'RMH': (9, 240, 390), 'RMK': (10, 230, 514), 'RMA': (11, 150, 620),
    'LBH': (12, 315, 465), 'LBK': (13, 166, 466), 'LBA': (14, 140, 620),
    'RBH': (15, 320, 480), 'RBK': (16, 209, 499), 'RBA': (17, 150, 676),
    'N': (18, 150, 650)
}

driver1 = PWM(0x40)
driver2 = PWM(0x41)
```

Or you may need to edit many of the lines in this file. For example this is what @patrickpoirier51 submitted as an issue: 
- https://github.com/mithi/hexy/issues/3

> I do have a different type of hexapod and the servo configuration makes the left and right side asymmetric, so +10 deg on left side makes -10 deg on right side. - @patrickpoirier51

Basically to solve his issue, he added a `direction` or a symmetry parameter at `joint_properties` IE
```
joint_properties = {

    'LFH': (0, 330, 480, -1), 'LFK': (1, 200, 515, -1), 'LFA': (2, 130, 610, 1),
    'RFH': (3, 380, 530, 1), 'RFK': (4, 300, 615, 1), 'RFA': (5, 130, 610, -1),
    'LMH': (6, 320, 470, -1), 'LMK': (7, 251, 531, -1), 'LMA': (8, 130, 610, 1),
    'RMH': (9, 380, 530, 1), 'RMK': (10, 290, 605, 1), 'RMA': (11, 150, 630, -1),
    'LBH': (12, 350, 500, -1), 'LBK': (13, 200, 515, -1), 'LBA': (14, 180, 660, 1),
    'RBH': (15, 350, 500, 1), 'RBK': (16, 300, 615, 1), 'RBA': (17, 130, 610, -1),
    'N': (18, 150, 650, 1)
    
```
And consequently updated the initialization of `Joint` in line `132`
```
    self.channel, self.min_pulse, self.max_pulse, self.direction = joint_properties[jkey]
```

As well as the `pose()` method in `Joint` in line `140`

```
    pulse = remap((angle * self.direction), (-self.max, self.max), (self.min_pulse, self.max_pulse))
```

Also equally important is the range of motion of each `Joint` which I've defined in line `87` of the `Leg` class.
The ankle has a range of motion from `-90 to 90` while the hip and knee's range is `-45, 45` and `-50, 50` respectively. 
I have a  knee leeway of 10 degrees. Change these as you see fit.
```
max_hip, max_knee, knee_leeway = 45, 50, 10
```


# SAMPLE USAGE
```
HexapodCore > Hexapod > HexapodPro > DancingHexapod
```
 
The easiest way to get this up and running, on your raspberry pi zero is to do the following on the terminal via ssh.

## Setup 
```
$ ssh YOUR.RPI.IP.ADDR -l pi 
$ cd /home/pi
$ git clone https://github.com/mithi/hexy.git
$ sudo python setup.py install
$ python -m hexy.demo.demo1
$ python -m hexy.demo.demo2
$ python -m hexy.demo.demo3
```

## High Level Usage

Sample usage when running python interpreter from anywhere in your system... 

```
>>> from hexy.robot.hexapod import Hexapod
>>> hexy = Hexapod()
>>> hexy.boot_up()
>>> hexy.walk(swing = 25, repetitions = 10)
>>> hexy.walk(swing = -25, repetitions = 10)
>>> hexy.rotate(offset = 40, repetitions = 7)
>>> hexy.rotate(offset = -40, repetitions = 7)
>>> hexy.shut_down()
```

Also try this...

```
>>> from hexy.robot.pro import HexapodPro
>>> hexy = HexapodPro()
>>> hexy.lie_flat()
>>> hexy.get_up()
>>> hexy.shake_head()
>>> hexy.wave()
>>> hexy.point()
>>> hexy.type_stuff()
>>> hexy.lie_down()
>>> hexy.off()
```

And this :)

```
>>> from hexy.robot.dancing import DancingHexapod
>>> hexy = DancingHexapod()
>>> hexy.boot_up()
>>> hexy.night_fever()
>>> hexy.default()
>>> hexy.dance_tilt()
>>> hexy.squat(angle = 60)
>>> hexy.thriller()
>>> hexy.lie_down()
>>> hexy.curl_up(die = True)
```

## Low Level Usage

If you want to control the angle of each `Joint` (`hip`, `knee`, `ankle`) for each `Leg` you'd want to instantiate a `HexapodCore` object:

```
>>> from hexy.robot.core import HexapodCore
>>> hexy = HexapodCore()
```

Each `Leg` can be access like this which is based in its position:

```
hexy.left_front
hexy.left_middle
hexy.left_back
 
hexy.right_front
hexy.right_middle
hexy.right_back
 
```

Whose three `Joints` you can individual pose using the `pose` command, for example:

```
hexy.right_front.pose(hip_angle = 0, knee_angle = 0, ankle_angle = 0)
hexy.right_front.off() # prevents servo overloading
```

There are also built-in lists of legs which you can iterate over:

```
hexy.legs # all six legs
hexy.right_legs 
hexy.left_legs
hexy.tripod1 # left front, right middle left back
hexy.tripod2 # right front, left middle, right back
```

For example:

```
for leg in hexy.right_legs:
  leg.hip.pose(angle = 0)
  leg.knee.pose(angle = 0)
  leg.ankle.pose(angle = 0)
  leg.off()

for leg in hexy.tripod1:
  leg.knee.pose(angle = 0)
  leg.knee.off()
```

You can also pose the `neck`:
```
hexy.neck.pose(angle = 90)
hexy.neck.off()
```
[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/minimithi)
