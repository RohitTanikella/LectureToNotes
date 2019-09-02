from transcribe import transcribe

link = "https://www.youtube.com/watch?v=0_LryzvBxFw" #CS61A First Lecture
lecture = transcribe(link)
print(lecture)