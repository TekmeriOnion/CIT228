import random
problems = int(input("How many math problems will you be solving? "))
counter = 0
numberCorrect = 0
while counter < problems:
    rando1 = random.randrange(1,1000)
    rando2 = random.randrange(1,1000)
    correctAnswer = int(rando1 + rando2)
    yourAnswer = int(input(f"\nWhat is the integer value of {rando1} + {rando2}? "))
    if correctAnswer == yourAnswer:
        print("Woo! Nailed it")
        numberCorrect += 1
    else:
        print("Dang, the correct answer is ",correctAnswer,)
    counter += 1
print(f"\nYou answered {numberCorrect} questions correctly!")
print("See you next time you need to pracitce your arithmetic!")