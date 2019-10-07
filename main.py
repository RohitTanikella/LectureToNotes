from transcribe import transcribe
from summarize import summary

#Make the link a command line argument so file does not have to be edited directly
link = "https://www.youtube.com/watch?v=0_LryzvBxFw" #CS61A First Lecture
lecture = transcribe(link)
summary = summary(lecture)

#print(summary)