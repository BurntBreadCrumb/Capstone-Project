#things I want my new fun dataframe compiler to do
#input=directories which contain all of my data :o
    #first: give one directory (7_23_22) and ask it to run birdnet on each file within East, South, and West
    #as it goes i want to save birdnet in a list, and also date and time to differentiate files
#output = dataframe containing all output (birdNET dataframe but also include the date (from file name) and time (also from file name))
    #will have to store all of the information in a list (with birdnetlib already days hooray) then convert the list into pandas df
# import required module
import os 
from pathlib import Path
import pandas as pd

# deploy birdnetlib
from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
from datetime import datetime

#def function = inputs: year and recorder direction and hourly? 
#should include a branch for one file or multiple files #WIP

directory = "TestDirectory/"
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
            print("x:", x)
            globallist.append(x) #please be recursive
            print("globallist:", globallist)
###create and write a selection table (txt)
print(globallist)
# specifying the columns makes sure they are in the desired order
df = pd.DataFrame(globallist, columns=['common_name', 'scientific_name', 'start_time', 'end_time', 'confidence', 'label', 'date', 'time', 'recorder'])
print(df) #CHECKPOINT

#EDIT FILENAME
name = "JuneDetections"
df.to_csv(name+'.txt',  sep='\t', index=False)


###https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
'''        data_folder = Path(directory)

        file_to_open = data_folder / file
        f = file_to_open 
'''