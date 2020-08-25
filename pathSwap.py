# Handler to convert windows created scripts to house a unix path
import sys
import numpy as np
import regex as re

# Variable linked with bash script
file = sys.argv[1]

# Function declaration
# Identify and convert path in file
def findPath(file):

    # Known path and file
    path = '/home/justinmiller/devel/'
    f = open(path + file, 'r')

    # Getting full string
    string = f.read()
    
    # Temporarily closing file
    f.close()

    # Getting index of c:\devel
    # Uncertainty in /\... search c and devel seperately
    # Initializing loc arrays
    devLoc = np.array([])
    cLoc = np.array([])

    # Starting loop
    # DevLoc
    for match in re.finditer("devel",string):
        devLoc = np.append(match.start(), devLoc)
     
    # CLoc
    for match in re.finditer("C:",string):
        cLoc = np.append(match.start(), cLoc)
    
    # Checking each devel:
    # Creating a list of found indices
    foundList = np.array([])

    # Looping through dev locations
    for i in range(len(devLoc)):

        # If c starts 3 before append found
        if devLoc[i] - 3 in cLoc:
            foundList  = np.append(foundList, devLoc[i]-3)
  
    # For each index found
    for idx in range(len(foundList)):
        # Convert that line
        convertLine(path, file, string, foundList[idx])

# Function to convert line
def convertLine(path, file, string, index):

    # Known linux path
    unixPath = "/home/justinmiller/devel"

    # Getting start and end times
    start = int(index)
    end = int(index + 8)

    # Replace old file with new string
    string = string.replace(string[start:end], unixPath)
    
    # Open file
    f = open(path + file, 'w')

    # We also need to change all slashes to / for linux
    string = string.replace("\\", '/')
    
    # Write New string
    f.write(string)

    # Closing file
    f.close()
    
# Running for the given file
findPath(file)
