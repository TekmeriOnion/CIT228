# Ch 10 Hands-On #4
import json

def toJson(glossary,filename):
    with open(filename, 'w') as f:
        json.dump(glossary,f,indent=4,sort_keys=True)

def readJson(filename):
    try:
        with open(filename, 'r') as f:
            reader = json.load(f)
    except FileNotFoundError:
        print("The file you are trying to read cannot be found. Please check your directory and try again")
    else:
        for k,v in reader.items():
            print(f"{k}: {v}")

def appendJson(filename,new_item):
    try: 
        with open(filename, 'r+') as f:
            glossary = json.load(f)
            glossary.update(new_item)
            f.seek(0)
            json.dump(glossary, f, indent=4,sort_keys=True)
            print("Data has been added to ",filename)
    except FileNotFoundError:
        print("The file you are trying to update cannot be found. Please check your directory and try again")

def menu():
    user_select = int(input("Enter -1- to create glossary json file, -2- to read from and print the glossary, -3- to add to the glossary, or -4- to quit: "))
    while user_select!=1 and user_select!=2 and user_select!=3 and user_select!=4:
        print(f"Sorry, {user_select} is not one of the menu options, please try again")
        user_select = int(input("Enter -1- to create glossary json file, -2- to read from and print the glossary, -3- to add to the glossary, or -4- to quit: "))
    return user_select

pyTerms = {
    'list':'ordered python data type that stores a mutable set of values and which allows duplicate entries', 
    'set':'unordered python data type which is mutable but does not allow duplicate entries', 
    'while loop':'a construct that performs an iterative set of tasks as long as specified conditions remain true', 
    'for loop':'a construct that performs an iterative set of tasks a discrete number of times',
    'break':'a command used to stop a while loop under certain conditions so it does not repeat infinitely',
    'dictionary':'an unordered data type consisting of a collection of key-value pairs',
    'string': 'a data type used for storing alphanumeric sequences as plain text',
    'slicing': 'a method for accessing specific portions of lists or strings',
    'modulo': 'a mathematical operation using the percent sign which returns the remainder yielded by dividing one integer by another',
    'index': 'a numerical value corresponding to a specific position within an ordered data structure like a string or list'
    }

choice = menu()
while choice != 4:
    if choice == 1:
        toJson(pyTerms,'pyTerms.json')
    elif choice == 2:
        readJson('pyTerms.json')
    elif choice == 3:
        newTerm = input("Enter a term to add to the glossary: ")
        if ' ' in newTerm:
            newTerm = newTerm.split()
            count = len(newTerm)
            termFixed = newTerm[0]
            for i in range(1,count):
                termFixed += newTerm[i].title()
            # print(termFixed)
        else:
            pass
        newDef = input("Enter the definition for your added term: ")
        newEntry = {termFixed:newDef}
        appendJson('pyTerms.json',newEntry)
    else:
        print("Your selection is unavailable - please try again")
    choice = menu()