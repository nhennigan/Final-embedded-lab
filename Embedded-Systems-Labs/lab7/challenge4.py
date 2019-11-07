from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255,0,0)
green = (0,255,0)
orange = (255,165,0)

while True:
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

	x = abs(x)
	y = abs(y)
	z = abs(z)

	if x > 1 and x < 2 or y > 1 and y < 2  or z > 1 and z < 2:
		sense.set_pixels(green)
	else if x > 2 and x < 3 or y > 2 and y < 3 or z > 2 and z < 3:
		for i in range(0,9)
			sense.set_pixels(orange)
			sense.clear
	 else if x > 4 and x < 4 or y > 3 and y < 4 or z > 3 and z < 4:
		sense.set_pixels(red)
