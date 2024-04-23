# import required module
import os 
from pathlib import Path
import pandas as pd

# deploy birdnetlib
from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
from datetime import datetime

directory = "6_29_22/South/"
#East, West, South
globallist = []

# iterate over files in that directory
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".wav"):
        print(filename) #CHECKPOINT
        #print(os.path.join(directory, filename)) #CHECKPOINT
        currentFile = directory+filename #path to the file perhaps
        # Load and initialize the BirdNET-Analyzer models.
        analyzer = Analyzer()

        recording = Recording(
            analyzer,
            currentFile,
            lat = 30.305750, 
            lon = -97.915639,
            min_conf = 0.7
        )
#Barton Creek Preserve: 30.305750, -97.915639
#datetime = datetime(year= fullYearInput, month=, day=), #strip off file name
        recording.analyze()
        output = recording.detections

        name = filename.rstrip(".wav")
        metaData = name.split("_")
        print(metaData)
        if metaData[0] == "SMM01681":
            audiomoth = "West"
        if metaData[0] == "SMM01688":
            audiomoth = "East"
        else:
            audiomoth = "South"
        for x in output:
            #print(type(x)) #is dictionary
            x["date"] = metaData[1]
            x["time"] = metaData[2]
            x["recorder"] = audiomoth
            globallist.append(x) #please be recursive
###create and write a selection table (txt)
# specifying the columns makes sure they are in the desired order
df = pd.DataFrame(globallist, columns=['common_name', 'scientific_name', 'start_time', 'end_time', 'confidence', 'label', 'date', 'time', 'recorder'])
#print(df) #CHECKPOINT

#EDIT FILENAME
name = "SouthJuneAudioDetections"
df.to_csv(name+'.txt',  sep='\t', index=False)
