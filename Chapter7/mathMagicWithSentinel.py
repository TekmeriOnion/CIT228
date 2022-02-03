import random

numberCorrect = 0
playOn = True

while playOn == True:
    rando1 = random.randrange(1,1000)
    rando2 = random.randrange(1,1000)
    correctAnswer = int(rando1 + rando2)
    yourAnswer = int(input(f"\nWhat is the integer value of {rando1} + {rando2}? "))
    if correctAnswer == yourAnswer:
        print("Woo! Nailed it")
        numberCorrect += 1
    else:
        print("Dang, the correct answer is ",correctAnswer,)
    quitter = input("\nDo you want to keep practicing math problems? (type 'q' to quit, any other key to keep practicing) ")
    if quitter.lower() == 'q':
        playOn = False

print(f"\nYou answered {numberCorrect} questions correctly!")
print("See you next time you need to pracitce your arithmetic!")