# import required module
import os
from pathlib import Path

# deploy birdnetlib
from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
from datetime import datetime

# loop files in this directory
directory = '2022_Recordings'

# iterate over files in that directory
for file in os.listdir(directory):
    
    filename = os.fsdecode(file)
    if filename.endswith(".wav"):
        print(filename)
        print(os.path.join(directory, filename)) #CHECKPOINT

        currentFile = str(file)
        # Load and initialize the BirdNET-Analyzer models.
        analyzer = Analyzer()

        recording = Recording(
            analyzer,
            currentFile,
            min_conf=0.25,
        )

        recording.analyze()
        output = recording.detections


        ###create and write a selection table (txt)
        import pandas as pd

        my_dict = output
        # specifying the columns makes sure they are in the desired order
        df = pd.DataFrame(my_dict, columns=['common_name', 'scientific_name', 'start_time', 'end_time', 'confidence', 'label'])

        print(df) #creates a selection table but does not include low and high frequency or species code ? important ?
        #difference between birdnetlib and birdnet analyzer

        df.to_csv(filename+'.txt', sep='\t', index=False)
        continue
    
    else:
        continue


###https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
'''        data_folder = Path(directory)

        file_to_open = data_folder / file
        f = file_to_open 
'''
###problem: can name all files inside directory now but cannot access files inside directory

        
