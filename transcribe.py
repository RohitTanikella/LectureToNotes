from os import system, remove
from subprocess import check_output
import re

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
   """Remove useless items in raw captions"""
   removed = []
   for i in range(len(raw_captions)):
      if raw_captions[i].strip() != '' and 'align:start position:0%' not in raw_captions[i]:
         removed.append(raw_captions[i].strip())
   return removed

def remove_brackets(raw_captions):
   """Remove any text inside angle brackets"""
   for i in range(len(raw_captions)):
      brackets = re.findall(r'<.*?\>', raw_captions[i])#Non Greedy Search for text between angle brackets
      for bracket in brackets:
         raw_captions[i] = raw_captions[i].replace(bracket,'')#Remove all text in brackets
   return raw_captions

raw_captions = remove_empty(raw_captions)#Get rid of new lines, spaces, and meaningless values
raw_captions = raw_captions[3:]#Remove first 3 elements (same in every caption
raw_captions = remove_brackets(raw_captions)#Get rid of time stamps and other useless content in brackets
print(raw_captions)