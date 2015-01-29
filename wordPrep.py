import os

inputDirectory = "C:/parsedTranscripts/"
transcripts = []
lessons = []

for root, dirs, files in os.walk(inputDirectory):
    lessons.append(dirs)

for lesson in lessons[0]:
    for root, dirs, files in os.walk(inputDirectory + lesson):
        for f in files:
            if f.endswith(".txt"):
                transcripts.append(inputDirectory + lesson + "/" + f)
                
file = open("oneBigFile.txt", "w")
for transcript in transcripts:
    source = open(transcript, "r")
    file.write("\n\n" + transcript.split("/")[-1].split(".")[0] + "\n")
    for line in source:
        file.write(line)
file.close()
    

