import json
import subprocess

from pytube import Search
from pytube import YouTube
from youtube_search import YoutubeSearch


rootpath = "/Users/sam/Desktop/Music"
song_list = []
song = 'Hype boy'
results = YoutubeSearch(song,max_results=1).to_json()
data = json.loads(results)

for i in data['videos']:
    print('https://youtube.com' + i['url_suffix']) 
    song_list.append('https://youtube.com' + i['url_suffix'])


# Get the YouTube video by its URL
yt = YouTube(song_list[0])

# Get the audio stream (in mp3 format)
audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()



# Download the audio stream to a local file
if audio_stream is not None:
    # Download the audio stream to a local file
    audio_stream.download()
else:
    print("No audio stream available in mp4 format")

audio_file = audio_stream.default_filename
subprocess.call(['ffmpeg', '-i', audio_file, 'example.mp3'])