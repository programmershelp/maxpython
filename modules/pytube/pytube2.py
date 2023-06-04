# youtube video title program in python
from pytube import YouTube
import requests
from io import BytesIO
from PIL import Image
 
# paste the YouTube video URL here
url = "https://www.youtube.com/watch?v=aJrPquHlyGE"
 
# create a YouTube object and get the video title
youtube = YouTube(url)
title = youtube.title
 
# Print the title of the video
print(title)