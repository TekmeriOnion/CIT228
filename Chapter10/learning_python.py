# Exercise 10-1
filename = "learning_python.txt"

with open(filename) as learnFile:
    pythonCan = learnFile.read()
print("---------File Output Using read() Method------------")
print(pythonCan)

print("\n---------File Output Using Line-Level Looping------------")
with open(filename) as learnFile:
    for line in learnFile:
        print(line)

print("\n---------File Output Using readlines() Method------------")
with open(filename) as learnFile:
    pythonLines = learnFile.readlines()
print("Original Line List: ",pythonLines,"\n")
for line in pythonLines:
    print(line)

# Exercise 10-2

print("\n---------Line-level Word Replacement--------")
with open(filename) as learnFile:
    pythonLines = learnFile.readlines()
print("Original List: ",pythonLines,"\n")
for line in pythonLines:
    updated = line.replace('Python','C')
    print(updated)
