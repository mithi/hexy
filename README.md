# raspberry-pi-hexy
arcbotics hexy hexapod robot frame with raspberry pi zero and adafruit 16 channel i2c servo driver
check http://hexyrobot.wordpress.com for details
 
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

sample usage: 

```
$ cd /home/pi/hexy
$ python 
>>> from hexy.robot.hexapod import Hexapod
>>> hexy = Hexapod()
>>> hexy.boot_up()
>>> hexy.walk(swing = 25, repetitions = 10)
>>> hexy.walk(swing = -25, repetitions = 10)
>>> hexy.rotate(offset = 40, repetitions = 7)
>>> hexy.rotate(offset = -40, repetitions = 7)
>>> hexy.shut_down()
```

also try the following...

```
>>> from hexy.robot.pro import HexapodPro
>>> hexy = HexapodPro()
>>> hexy.lie_flat()
>>> hexy.get_up()
>>> hexy.default()
>>> hexy.shake_head()
>>> hexy.wave()
>>> hexy.point()
>>> hexy.dance_tilt()
>>> hexy.default()
>>> hexy.lie_down()
>>> hexy.off()
```

and this :)

```
>>> from hexy.robot.dancing import DancingHexapod
>>> hexy = DancingHexapod()
>>> hexy.boot_up()
>>> hexy.thriller()
>>> hexy.night_fever()
>>> hexy.lie_down()
>>> hexy.curl_up(die = True)
```
