from os import system
link = "https://www.youtube.com/watch?v=0_LryzvBxFw" #CS61A First Lecture
system("youtube-dl --write-auto-sub --skip-download " + link)
#system("youtube-dl --list-subs --skip-download " + link)