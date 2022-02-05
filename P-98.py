import os
import shutil

source = input("Enter Source Folder :- ")
destination = input("Enter Destination Folder :- ")
source = source + '/' 
destination = destination + '/' 

listOfFiles = os.listdir(source)
 
for file in listOfFiles:
    shutil.copy((source + file), destination)