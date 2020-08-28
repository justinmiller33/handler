# Just a script to print github password
# Will call script with keyboard shortcut to use with other git handlers

# Imports
import pyautogui

# Read path to local gitBash text file with info
f = open("/home/justinmiller/Desktop/gitBash.txt",'r')

# Get content
content = f.read()

# Get 40 digit key after =
idx = content.find("=")
key = content[idx+1:idx+41]

# Type with pyautogui
pyautogui.write(key)
