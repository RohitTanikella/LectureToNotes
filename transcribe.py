from os import system, remove
from subprocess import check_output

link = "https://www.youtube.com/watch?v=0_LryzvBxFw" #CS61A First Lecture
system("youtube-dl --write-auto-sub --skip-download " + link) #Download automated subtitles

title = check_output("youtube-dl --get-title --skip-download " + link, shell = True) #Store the video title
title = str(title.decode("utf-8")).strip() #Convert from bytes to string (utf-8) and strip the new line
video_id = link[link.index("v=")+2:] #Get video id from link
file_name = title + "-" + video_id + ".en.vtt" #Subtitle file name

with open(file_name) as f:
   raw_captions = f.readlines()

remove(file_name)#Delete file after reading subtitles from it

def remove_empty(raw_captions):
   "Remove empty items in raw captions"
   removed = []
   for i in range(len(raw_captions)):
      if raw_captions[i].strip() != '':
         removed.append(raw_captions[i].strip())
   return removed

raw_captions = remove_empty(raw_captions)#Get rid of new lines, spaces, and empty values
raw_captions = raw_captions[3:]#Remove first 3 elements (same in every caption
