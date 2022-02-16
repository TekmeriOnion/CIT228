# Exercises 10-6 and 10-7
print("Let's add some numbers!")
checker = ""
while checker != 'q':
    num1 = input("Enter a number: ")
    num2 = input("Enter another number you'd like to add to the first one: ")
    try: 
        total = int(num1)+int(num2)
        print(f"The sum of your two numbers is {total}")
        checker = input("Would you like to run another sum ('q' to quit):")
    except:
        print("Hm, seems that one of your entries was not a number. Try again using numerical values.")
        checker = input("Would you like to run another sum? ('q' to quit):")