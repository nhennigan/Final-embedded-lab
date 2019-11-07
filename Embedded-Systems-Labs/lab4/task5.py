
import time 

seconds_left = int(input('enter number of seconds: ')

while seconds_left > 0:
	minutes = int(round(seconds_left/60))
	seconds = int(seconds_left%60)
	if minutes < 10:
		minutes = str(0) + str(minutes)
	if seconds < 10:
 		seconds = str(0) + str(seconds)

	print(str(minutes) + ":" + str(seconds))

  	seconds_left -=1
  	time.sleep(1)





