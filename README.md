
Arcbotics hexapod robot frame with Raspberry Pi Zero and Adafruit 16 channel I2C servo driver
- [Hexy Documentation](http://hexyrobot.wordpress.com)
- [Hexy Transcript](https://medium.com/@mithi/a-raspberry-pi-hexy-transcript-62533c69a566)

```
HexapodCore > Hexapod > HexapodPro > DancingHexapod
```
 
the easiest way to get this up and running, on your raspberry pi zero is to do the following on the terminal via ssh.

```
$ ssh YOUR.RPI.IP.ADDR -l pi 
$ cd /home/pi
$ git clone https://github.com/mithi/hexy.git
$ sudo python setup.py install
$ python -m hexy.demo.demo1
$ python -m hexy.demo.demo2
$ python -m hexy.demo.demo3
```

sample usage when running python interpreter from anywhere in your system... 

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

also try this...

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

and this :)

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
