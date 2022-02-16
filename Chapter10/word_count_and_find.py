def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

# Exercise 10-10

def find_words(filename,searched):
    """Count the number of times a specified word appears in a text"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        contents = contents.lower()
        searched = str(searched).lower() + " "
        counted = contents.count(searched)
        print(f"The word, {searched.strip()}, appeared {counted} times in {filename}.")

filenames = ['frankensteinCh1.txt', 'down_the_rabbit_hole.txt', 'scandal_in_bohemia.txt']
for filename in filenames:
    count_words(filename)

searchWord = input("\nPlease enter the word you'd like to search for: ")
for f in filenames:
    find_words(f,searchWord)