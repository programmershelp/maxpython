#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont

myImage = Image.new("RGB", (512, 512), (0, 0, 0)) #black background

draw = ImageDraw.Draw(myImage)

draw.line((0, myImage.height, myImage.width, 0), fill=(255, 0, 0), width=6) #red line 
draw.rectangle((70, 70, 200, 200), fill=(0, 255, 0)) #green rectangle
draw.ellipse((250, 400, 450, 500), fill=(0, 0, 255)) #blue ellipse
draw.multiline_text((50, 50), 'Pillow sample', fill=(255, 255, 255)) #white text

myImage.save('C:\\Python38-32\\draw.jpg')



