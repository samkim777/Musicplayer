import tkinter as tk
import fnmatch 
import os
import pygame
from pygame import mixer


canvas = tk.Tk()
canvas.title('Music Player')
canvas.geometry('800x900')
canvas.config(bg='black')

song_count = 0
loaded = False
paused = False

pygame.init()




rootpath = "/Users/sam/Desktop/Music"
pattern = '*.mp3'

mixer.init()




def select(): 
    song = listbox.curselection()
    song_name = listbox.get(song[0])
    label.config(text = listbox.get(song))
    mixer.music.load(rootpath + '/' + song_name)
    mixer.music.play()
    global loaded
    loaded = True
    print(song[0])

def stop():
    mixer.music.stop()
    label.config(text = '')
    listbox.select_clear('active')

def next():
    next_song = listbox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listbox.get(next_song)
    label.config(text = next_song_name)
    
    listbox.select_clear(0,'end')
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
        paused = True
        mixer.music.pause()
        pauseButton['text'] = 'Resume' # Change next incident of button to Resume    
    else: 
        mixer.music.unpause()
        paused = False
        pauseButton['text'] = 'Pause'           

 
def loop():    
    if not mixer.music.get_busy() and loaded and paused == True: # Song not playing
       cur_song = listbox.curselection()

       # Not at the last song
       if cur_song[0] + 1 <= song_count - 1: 
        next_song = cur_song[0] + 1 
        label.config(text = listbox.get(next_song))
        mixer.music.load(rootpath + "/" + listbox.get(next_song))
        mixer.music.play()

        listbox.select_clear(0,'end')
        listbox.activate(next_song)
        listbox.select_set(next_song)

       # At the last song 
       if cur_song[0] + 1 > song_count - 1:  
        next_song = 0 
        label.config(text = listbox.get(next_song))
        mixer.music.load(rootpath + "/" + listbox.get(next_song))
        mixer.music.play()
        listbox.select_clear(0,'end')
        listbox.activate(next_song)
        listbox.select_set(next_song)

       

    canvas.after(3000,loop) 



listbox = tk.Listbox(canvas, fg = 'green', bg = "cyan", width= 400, font = ('poppins', 14))
listbox.pack(padx = 15, pady = 15)

label = tk.Label(canvas, text = '', bg = 'black', fg = 'white', font = ('poppins', 30))
label.pack(pady = 30)

align = tk.Frame(canvas, bg = 'black')
align.pack(padx = 10, pady = 50, anchor = 'center')

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
        listbox.insert(0,filename) 
        song_count += 1 # Get current song list size


canvas.after(1000,loop())
canvas.mainloop()