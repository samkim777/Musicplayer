import json
import subprocess

from pytube import Search
from pytube import YouTube
from youtube_search import YoutubeSearch
from melonapi import scrapeMelon

song_list = []
song_list_url = [] 
rootpath = "/Users/sam/Desktop/Music"
mp4path = "/Users/sam/Desktop/MusicMp4" 


# Grab JSON of currently top 100 trending songs from melon
songs = json.loads(scrapeMelon.getList("LIVE").decode())

for song_name in songs.items():
    # Search youtube for this song
    results = YoutubeSearch(song_name[1]['name'] + ' ' + 'lyrics',max_results=1).to_json()

    # Load json data
    data = json.loads(results)
    for i in data['videos']: # From JSON, look at the url suffix
        # Add song url to song_list
        song_list_url.append('https://youtube.com' + i['url_suffix']) 


for url in song_list_url:
    # Grab youtube object
    yt = YouTube(url)
    # Extract audio only
    audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

    if audio_stream is not None:
        # Download the audio stream to a local file
        audio_stream.download(mp4path)
        # Get audio filename
        audio_file = audio_stream.default_filename
        # Turn mp4 into mp3 for compatibility
        subprocess.call(['ffmpeg', '-i', mp4path +'/' + audio_file, "-vn", "-acodec", "mp3", "-ar",
        "44100", "-ss", "0", "-b:a", "320k" ,rootpath + '/' + audio_file])
    else:
        print("No audio stream available in mp4 format")


    




