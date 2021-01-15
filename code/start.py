print("Bot-> Please wait, while I get ready ...")

import re, sys, os
from ProcessContext import ProcessContext as PC
from ProcessQuestion import ProcessQuestion as PQ
from Utilities import Utilities as UT

instead_use_lemmanization = False

print("Bot-> I have 2 modes in which i can run")
print("Bot-> 1) Data Specific questions - Here you can chosse the category of the data")
print("Bot-> 2) Overall questions - Here you ask the questions and i will decide which category will it belong to")
print("Bot-> Please Choose :- ", end = "")

specific = False
databasename = ""
possible_db_name = os.listdir('../dataset')
ut = UT()

def properInput(x):
    global specific
    if x == '1' or x == '2':
        if x == '1':
            specific = True
        return True
    else:
        print("Please choose a proper input - Either 1 or 2 - ", end = "")
        return False

def properDatabaseName(x, possible_db_name):
    global databasename
    if x in possible_db_name:
        databasename = x
        return True
    else:
        print("Please choose a proper database name - ", end = "")
        return False
    
while True:
    inp = input()
    if properInput(inp):
        break
    
if specific:
    print("Bot-> Please name the Database name - ", end = "")
    while True:
        inp2 = input()
        if properDatabaseName(inp2, possible_db_name):
            break
    try:
        file = open('../dataset/'+databasename,"r", encoding='utf-8')
        specificDatalines = []
        for line in file.readlines():
            if(len(line.strip()) > 0):
                specificDatalines.append(line.strip())
        specificData = PC(specificDatalines)
    except FileNotFoundError:
        print("Bot> Oops! Currently i dont have \"" + databasename + "\""+" in my database set")
        exit()

# Loading Dataset


print("Bot-> Please wait while i get all the required data ready")
# print(specific)
docs = {}
if not specific:
    for name in possible_db_name:
        docs[name] = {}
        docs[name]['data'] = []
        
        with open('../dataset/'+name,"r", encoding='utf-8') as f:
            for line in f.readlines():
                if(len(line.strip()) > 0):
                    docs[name]['data'].append(line.strip())
                    
        docs[name]['contextobj'] = PC(docs[name]['data'])

# print(len(specificData.paraInfo))
# print(specificData.paraInfo[0]['paraVector'])
print("Bot-> Hey there! Thanks for your patience. Please ask factoid based questions only :P")
print("Bot-> You can say me Bye anytime you want")

# Greet Pattern
greetPattern = re.compile("^\ *((hey)|(hi+)|((good\ )?morning|evening|afternoon)|(he((llo)|y+)))\ *$",re.I)
exitPattern = re.compile("^\ *((bye*\ ?)|(see (you|ya) later))\ *$",re.I)

while True:
    response = ""
    userInp = input("You-> ")
    if not len(userInp) > 0:
        response = "Please enter valid question."
    elif greetPattern.match(userInp):
        response = "Hello!"
    elif exitPattern.match(userInp):
        response = "See ya next time!"
        print("Bot-> ", response)
        break
    else:
        if specific:
            print(len(specificData.paraInfo))
            response = "Going deep"
        else:
            closestvector, obj = ut.GetClosestContextFile(1)
            if closestvector == 0:
                response = "Please provide a better question with more context"
            else:
                response = "Going wide"
    print("Bot-> ", response)
    
