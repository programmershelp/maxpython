# Download youtube audio in python
from pytube import YouTube
 
# Set the URL of the video you want to download
url = "https://www.youtube.com/watch?v=aJrPquHlyGE"

# Create a YouTube object
yt = YouTube(url)
 
# Filter for streams that only contain audio
audio_stream = yt.streams.filter(only_audio=True)
print(audio_stream)
 
# set the download path
download_path = "O:\\"

# Download the first stream in the list
audio_stream[0].download(download_path)