
import os
import pygame
from moviepy.editor import *
from pathlib import Path

home = Path.home()
path = home.joinpath("music")
print(path)
#path = "/Users/metinkaratas/music"

dir_list = os.listdir(path)

for i in range(len(dir_list)):
    print("{} - {}".format(i,dir_list[i]))

selection = int(input("Bitte geben Sie eine Zahl ein: "))
filetoplay = path.joinpath(dir_list[selection])
#filetoplay = path + "/" + (dir_list[selection])
print(filetoplay)

filetoplay = str(filetoplay)
pygame.init()

if filetoplay.endswith(".mp3"):
    pygame.mixer.init()
    pygame.mixer.music.load(filetoplay)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
elif filetoplay.endswith(".mp4"):
    pygame.display.set_caption('Movie')
    clip = VideoFileClip(filetoplay)
    clip.preview()
else:
    print("Datei kann nicht wiedergegeben werden.")

pygame.quit()