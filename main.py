from transcribe import transcribe
from summarize import summary

link = "https://www.youtube.com/watch?v=0_LryzvBxFw" #CS61A First Lecture
lecture = transcribe(link)
summary = summary(lecture)

print(summary)