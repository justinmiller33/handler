# Handler to convert unix path back to windows
import sys
import numpy as np

# Linked from bash script
file = sys.argv[1]

# Known path and file
path = '/home/justinmiller/devel/'
f = open(path + file, 'r')

# Reading
string = f.read()

# Closing
f.close()

# Replacing string with windows path
string = string.replace('/home/justinmiller/','C:/')

# Reopen and write new string
f = open(path + file, 'w')
f.write(string)
f.close()
