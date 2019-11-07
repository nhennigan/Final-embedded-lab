
from sense_hat import SenseHat
from time import sleep
def clear_leds(sense):

0 = [255,255,255]
cleared = [
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0]
sense.set_pixles(cleared)

 ##
## Reset the values of the sensehat to 0
 ##
sense = SenseHat()
clear_leds(sense)

sense.set_pixels(1,4,255,0,0)
sense.set_pixels(2,4,255, 0, 0)
sense.set_pixels(3,4,255, 0, 0)
sense.set_pixels(4,4,255, 0, 0)
sense.set_pixels(5,4,255, 0, 0)
sense.set_pixels(3,3,0, 255, 0)
sense.set_pixels(3,4,0, 255, 0)
sense.set_pixels(3,5,0, 255, 0)
sense.set_pixels(3,6,0, 255, 0)

sense.set_pixel(1,4,(255,0,0))
sense.set_pixel(2,4,(255, 0, 0))
sense.set_pixel(3,4,(255, 0, 0))
sense.set_pixel(4,4,(255, 0, 0))
sense.set_pixel(5,4,(255, 0, 0))
sense.set_pixel(3,3,(0, 255, 0))
sense.set_pixel(3,4,(0, 255, 0))
sense.set_pixel(3,5,(0, 255, 0))
sense.set_pixel(3,6,(0, 255, 0))
sense.set_pixel(3,2,(0, 255, 0))





## Insert code HERE ##
## Commands for image
## Added code ends HERE ##
#sense.flip_v()
angle=0
while True:
 if angle>270:
 angle=0
 sense.set_rotation(angle)
 sleep(1)
 angle+=90
