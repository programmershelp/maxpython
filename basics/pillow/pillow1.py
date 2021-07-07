#!/usr/bin/python

from PIL import Image, ImageFilter
import sys

try:
    myImage = Image.open("C:\\Python38-32\\snake.png")
except IOError:
    print("Unable to load image")
    sys.exit(1)
	
grayImage = myImage.convert('L')
grayImage.show()



