import pandas as pd
'''Compare species detections between BirdNET and ebird and TNC point counts'''

#TNC pointcounts (April-May 2022)
TNC = ["Chipping Sparrow", "Painted Bunting", "Northern Cardinal", "White-eyed Vireo", "Mourning Dove", 
       "Blue-gray Gnatcatcher", "Golden-cheeked Warbler", "Tufted Titmouse", "Northern Mockingbird"] #unidentified hummingbird
#EBIRD HOTSPOTS
#Barton Creek Habitat Preserve (April-July 2022)
bchp = ["Clay-colored Sparrow", "Hutton's Vireo", "Rufous-crowned Sparrow", "Woodhouse's Scrub-Jay", 
        "Yellow-breasted Chat", "Black-capped Vireo", "Orchard Oriole", "Cave Swallow"]
#Commons Ford Ranch Metropolitan Park (April-July 2022)
cfrmp = ["Scarlet Tanager", "Golden-winged Warbler", "Pectoral Sandpiper", "Black-billed Cuckoo"]
#Mary Quinlan Park (May-July 2022)
mqp = ["Painted Bunting", "Summer Tanager", "Purple Martin"]

surveyData = [bchp, cfrmp, mqp, TNC]
'''different directories/datasets'''
#df = pd.read_csv('EastJuneAudioDetections.txt', sep="\t")
#df = pd.read_csv('SouthJuneAudioDetections.txt', sep="\t")
#df = pd.read_csv('WestJuneAudioDetections.txt', sep="\t")

name = ["EastJune_bchp", "EastJune_cfrmp", "EastJune_mqp", "EastJune_TNC"]
#name = ["SouthJune_bchp", "SouthJune_cfrmp", "SouthJune_mqp", "SouthJune_TNC"]
#name = ["WestJune_bchp", "WestJune_cfrmp", "WestJune_mqp", "WestJune_TNC"]

for i in range(len(surveyData)):
    print(surveyData[i])
    df2 = df.loc[df['common_name'].isin(surveyData[i])] #dataframe with common species between birdnet and TNC/ebird
    print(df2)
    df2.to_csv(name[i]+'.csv',  sep=',', index=False) #write to csv file

#print(df.loc[df['common_name'] == "Red-eyed Vireo"]) #test value