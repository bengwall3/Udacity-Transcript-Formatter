import os
from zipfile import ZipFile        

def parseTranscript(inputLines, outputFile):
    lines = [""] + [line.decode("utf-8") for line in inputLines]

    writeThese = [""]
    
    for i in range(len(lines)):
        if i % 4 == 3:
            line = lines[i]
            if line[0] == ">":
                writeThese[-1] += "\n"
            writeThese.append(line + " ")
            
    foo = [outputFile.write(line) for line in writeThese]

def checkOrMake(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
inputDirectory = "C:/transcripts/"
lessonZips = []

for root, dirs, files in os.walk(inputDirectory):
    for file in files:
        if file.endswith(".zip"):
            lessonZips.append(file[:-4])
            
outputDirectory = "C:/parsedTranscripts/"

checkOrMake(outputDirectory)

for lesson in lessonZips:
    checkOrMake(outputDirectory + lesson + "/")
    zipFile = ZipFile(inputDirectory + lesson + ".zip", "r")
    transcriptList = ZipFile.namelist(zipFile)
    for transcript in transcriptList:
        transcriptName = transcript[:-4]
        
        inputFile = zipFile.open(transcript, "r")
        inputLines = inputFile.readlines()
        outputFile = open(outputDirectory + lesson + "/" + transcriptName + ".txt", "w")
        
        parseTranscript(inputLines, outputFile)
        
        inputFile.close()
        outputFile.close()
