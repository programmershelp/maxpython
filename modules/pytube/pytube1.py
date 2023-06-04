# youtube downloader python script
from pytube import YouTube
import requests
from io import BytesIO
from PIL import Image
 
# paste the YouTube video URL here
url = "https://www.youtube.com/watch?v=aJrPquHlyGE"
 
# create a YouTube object and get the video thumbnail and title
youtube = YouTube(url)
# Get the URL of the video's thumbnail image
thumbnail_url = youtube.thumbnail_url
 
# display the thumbnail image and title
response = requests.get(thumbnail_url)
img = Image.open(BytesIO(response.content))
img.show()