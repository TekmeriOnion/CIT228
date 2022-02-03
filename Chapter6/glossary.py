print("------------------Exercise 6-3-------------------------")
glossary = {
    'list':'ordered python data type that stores a mutable set of values and which allows duplicate entries', 
    'set':'unordered python data type which is mutable but does not allow duplicate entries', 
    'while loop':'a construct that performs an iterative set of tasks as long as specified conditions remain true', 
    'for loop':'a construct that performs an iterative set of tasks a discrete number of times',
    'break':'a command used to stop a while loop under certain conditions so it does not repeat infinitely'
    }

print('list:')
print(f'\t{glossary["list"]}\n')
print('set:')
print(f'\t{glossary["set"]}\n')
print('while loop:')
print(f'\t{glossary["while loop"]}\n')
print('for loop:')
print(f'\t{glossary["for loop"]}\n')
print('break:')
print(f'\t{glossary["break"]}\n')

print("------------------Exercise 6-4-------------------------")
glossary["dictionary"] = "an unordered data type consisting of a collection of key-value pairs"
glossary["string"] = "a data type used for storing alphanumeric sequences as plain text"
glossary["slicing"] = "a method for accessing specific portions of lists or strings"
glossary["modulo"] = "a mathematical operation using the percent sign which returns the remainder yielded by dividing one integer by another"
glossary["index"] = "a numerical value corresponding to a specific position within an ordered data structure like a string or list"
for term , definition in glossary.items():
    print(f"\n{term}:")
    print(f"\t{definition}")