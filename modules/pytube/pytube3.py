# Explore Stream Types to download youtube videos using python
from pytube import YouTube
 
# paste the YouTube video URL here
url = "https://www.youtube.com/watch?v=aJrPquHlyGE"
 
# get the list of available streams
youtube = YouTube(url)
streams = youtube.streams.all()
 
# Print all stream types
print(streams)