import os
from zipfile import ZipFile

#Place all .zip files from Udacity in the directory you specify below:
inputDirectory = "C:/transcripts/"

#The formatted .txt files from each of the lessons will be saved in the directory you specify below:
outputDirectory = "C:/parsedTranscripts/"

def parseTranscript(inputLines, outputFile):
    lines = [""] + [line.decode("utf-8") for line in inputLines]

    writeThese = [""]
    
    for i in range(len(lines)):
        if i % 4 == 3:
            line = lines[i]
            if line[0] == ">":
                writeThese[-1] += "\n"
            writeThese.append(line + " ")
            
    for line in writeThese:
        outputFile.write(line)

def checkOrMake(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
lessonZips = []

for root, dirs, files in os.walk(inputDirectory):
    for f in files:
        if f.endswith(".zip"):
            lessonZips.append(f[:-4])

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
