from sense_hat import SenseHat
from time import sleep
from PIL import Image
import numpy as np
#import scipy.io


def load_image(values,sense):
pixel_width = 6
image_width = pixel_width*8
sense_pixels = []
start_pixel = 0
while start_pixel < (image_width*64):
    sense_pixels.extend(values[start_pixel:(
start_pixel+image_width):pixel_width])
    start_pixel += (image_width*pixel_width)
sense.set_pixels(sense_pixels)


 ## ##
## Insert code Here ##
 ## ##
def clear_leds(sense):
 ##
## Reset the values of the sensehat to 0
 ##
path_to_file = “Link to image file”
im = Image.open(path_to_file)
rgb_im=im.convert('RGB')
values=np.array(rgb_im)
sense=SenseHat()
clear_leds(sense)
load_image(values,sense)
sense.flip_v()
sense.set_rotation(270)
