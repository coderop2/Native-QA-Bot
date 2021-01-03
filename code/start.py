print("Bot-> Please wait, while I get ready ...")

import re
import sys

print("Bot-> I have 2 modes in which i can run")
print("Bot-> 1) Data Specific questions - Here you can chosse the category of the data")
print("Bot-> 2) Overall questions - Here you ask the questions and i will decide which category will it belong to")
print("Bot-> Please Choose :- ", end = "")

specific = False

def properInput(x):
    global specific
    if x == '1' or x == '2':
        if x == '1':
            specific = True
        return True
    else:
        print("Please choose a proper input - Either 1 or 2 - ", end = "")
        return False

while True:
    inp = input()
    if properInput(inp):
        break
    
print(specific)
datasetName = sys.argv[1]
# Loading Dataset

try:
	datasetFile = open(datasetName,"r")
except FileNotFoundError:
	print("Bot> Oops! I am unable to locate \"" + datasetName + "\"")
	exit()
