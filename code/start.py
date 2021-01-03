print("Bot-> Please wait, while I get ready ...")

import re
import sys

print("Bot-> I have 2 modes in which i can run")
print("Bot-> 1) Data Specific questions - Here you can chosse the category of the data")
print("Bot-> 2) Overall questions - Here you ask the questions and i will decide which category will it belong to")
print("Bot-> Please Choose :- ", end = "")

specific = False
databasename = ""
possible_db_name = ['New_York_City',
                 'Buddhism',
                 'Queen_Victoria',
                 'Modern_history',
                 'Windows_8',
                 'USB',
                 'Marvel_Comics',
                 'Mammal',
                 'Alloy',
                 'Rajasthan',
                 'Northwestern_University',
                 'Anthropology']

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

# Loading Dataset
try:
    file = open('../dataset/'+databasename+'.txt',"r")
except FileNotFoundError:
	print("Bot> Oops! Currently i dont have \"" + databasename + "\""+" in my database set")
	exit()

print("Bot-> Please wait while i get all the required data ready")

paragraphs = {}
for name in possible_db_name:
    paragraphs[name] = []
    with open('../dataset/'+name+'.txt',"r") as f:
        for line in f.readlines():
            if(len(line.strip()) > 0):
                paragraphs[name].append(line.strip())


print("Bot> Hey there! Thanks for your patience. Please ask factoid based questions only :P")
print("Bot> You can say me Bye anytime you want")

# Greet Pattern
greetPattern = re.compile("^\ *((hi+)|((good\ )?morning|evening|afternoon)|(he((llo)|y+)))\ *$",re.IGNORECASE)

while True:
    response = ""
    userInp = input("You-> ")
    if not len(userInp) > 0:
        response = "Bot-> Please enter valid question."
    elif greetPattern.findall(userQuery):
        response = "Hello!"
    elif userInp.strip().lower() == "bye":
        response = "See ya next time!"
        print("Bot-> ", response)
        break
    else:
        if specific:
            print("Going deep")
        else:
            print("Going wide")
    print("Bot-> ", response)
    
