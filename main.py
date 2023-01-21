import tkinter as tk
import fnmatch 
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title('Music Player')
canvas.geometry('400x600')
canvas.config(bg='black')

rootpath = "/Users/sam/Desktop/Music"
pattern = '*.mp3'

mixer.init()

def select(): 
    label.config(text = listbox.get('anchor'))
    mixer.music.load(rootpath + "/" + listbox.get('anchor'))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listbox.select_clear('active')

def next():
    next_song = listbox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listbox.get(next_song)
    label.config(text = next_song_name)
    
    listbox.select_clear('active')
    listbox.activate(next_song)
    listbox.select_set(next_song)

    mixer.music.load(rootpath + "/" + next_song_name)
    mixer.music.play()

def previous():
    prev_song = listbox.curselection()
    prev_song = prev_song[0] - 1
    prev_song_name = listbox.get(prev_song)
    label.config(text = prev_song_name)

    listbox.select_clear('active')
    listbox.activate(prev_song)
    listbox.select_set(prev_song)

    mixer.music.load(rootpath + '/' + prev_song_name)
    mixer.music.play()    

def pause():
    if  pauseButton['text'] == 'Pause':
        mixer.music.pause()
        pauseButton['text'] = 'Resume' # Change next incident of button to Resume    
    else: 
        mixer.music.unpause()
        pauseButton['text'] = 'Pause'

listbox = tk.Listbox(canvas, fg = 'green', bg = "cyan", width= 400, font = ('ds-digital',14))
listbox.pack(padx = 15, pady = 15)

label = tk.Label(canvas, text = '', bg = 'black', fg = 'blue', font = ('ds-digital',40))
label.pack(pady = 15)

align = tk.Frame(canvas, bg = 'black')
align.pack(padx = 10, pady =10, anchor = 'center')

prevButton = tk.Button(canvas, text = 'Prev', command = previous)
prevButton.pack(pady = 10, in_ = align , side = 'left')

stopButton = tk.Button(canvas, text = 'Stop', command = stop)
stopButton.pack(pady = 10, in_ = align , side = 'left')

playButton = tk.Button(canvas, text = 'Play', command = select)
playButton.pack(pady = 10, in_ = align , side = 'left')

pauseButton = tk.Button(canvas, text = 'Pause', command = pause)
pauseButton.pack(pady = 10, in_ = align , side = 'left')

nextButton = tk.Button(canvas, text = 'Next', command = next)
nextButton.pack(pady = 10, in_ = align , side = 'left')


for root,dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listbox.insert('end',filename) 

canvas.mainloop()