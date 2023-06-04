# Download youtube video
from pytube import YouTube
 
# paste the YouTube video URL here
url = "https://www.youtube.com/watch?v=aJrPquHlyGE"
 
# create a YouTube object and get the video stream
youtube = YouTube(url)
video_stream = youtube.streams.filter(res="720p")
print(video_stream)
 
# set the download path and download the video
download_path = "O:\\"
video_stream.first().download(download_path)