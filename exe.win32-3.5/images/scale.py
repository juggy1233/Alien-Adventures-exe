from pygame import *

init()

img = 'icon.png'

image.save(transform.scale(image.load(img), (256,256)), 'new_img.png')