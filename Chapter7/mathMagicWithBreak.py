import random

counter = 0
numberCorrect = 0
numberIncorrect = 0

while counter < 10:
    rando1 = random.randrange(1,1000)
    rando2 = random.randrange(1,1000)
    correctAnswer = int(rando1 - rando2)
    yourAnswer = int(input(f"\nWhat is the integer value of {rando1} - {rando2}? "))
    
    if numberIncorrect > 5:
        print("""\nYou've answered more than five problems incorrectly. 
NMC has a great Tutoring department, you can make an appointment by emailing tutoring@nmc.edu!""")
        break
    
    else:
        if correctAnswer == yourAnswer:
            print("Woo! Nailed it")
            numberCorrect += 1
            counter += 1
        else:
            print("Dang, the correct answer is ",correctAnswer,)
            numberIncorrect += 1
            counter += 1
print(f"\nYou answered {numberCorrect} questions correctly and {numberIncorrect} questions incorrectly")
print("See you next time you need to pracitce your arithmetic!")