import time
# Get input from user
seconds_left = int(input('Enter number of seconds: '))
while seconds_left > 0:
  minutes = int(round(seconds_left/60)) # Get number of minutes
  seconds = int(seconds_left%60) # Get number of seconds
  if minutes < 10:
    minutes = str(0) + str(minutes)
  if seconds < 10:
    seconds = str(0) + str(seconds)
# Print counter value to screen
  print(str(minutes) + ":" + str(seconds))
  seconds_left -=1 # Decrement number of seconds left
  time.sleep(1) # Sleep for 1 second
