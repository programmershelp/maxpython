from pytube import YouTube
 
# paste the YouTube video URL here
url = "https://www.youtube.com/watch?v=aJrPquHlyGE"
 
# create a YouTube object and get the video stream
youtube = YouTube(url)
 
resolutions = ['144p', '240p', '360p', '480p', '720p', '1080p']
 
for resolution in resolutions:
    streams = youtube.streams.filter(progressive=True, res=resolution)
     
    if len(streams) > 0:
        print(resolution)
    else:
        print(resolution + ' Audio is not available')