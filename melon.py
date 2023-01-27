import json
import subprocess

from pytube import Search
from pytube import YouTube
from youtube_search import YoutubeSearch
from melonapi import scrapeMelon


rootpath = "/Users/sam/Desktop/Music"
mp4path = "/Users/sam/Desktop/MusicMp4"
song_list = []
song = 'Hype boy'
results = YoutubeSearch(song,max_results=1).to_json()
data = json.loads(results)






for i in data['videos']: # From JSON, look at the url suffix
    print('https://youtube.com' + i['url_suffix']) 
    # Add song url to song_list
    song_list.append('https://youtube.com' + i['url_suffix']) 


# Get the YouTube video by its URL
yt = YouTube(song_list[0])

# Get the audio stream (in mp4 format)
audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()



# Download the audio stream to a local file
if audio_stream is not None:
    # Download the audio stream to a local file
    audio_stream.download(mp4path)
else:
    print("No audio stream available in mp4 format")

# Get audio filename
audio_file = audio_stream.default_filename
# Turn mp4 into mp3 for compatibility
subprocess.call(['ffmpeg', '-i', mp4path +'/' + audio_file, "-vn", "-acodec", "mp3", "-ar",
 "44100", "-ss", "0", "-b:a", "320k" ,rootpath + '/' + song + '.mp3'])
# Time of song is doubled why?


