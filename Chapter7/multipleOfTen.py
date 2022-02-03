checkNum = input("Please enter an integer to find out if it is a multiple of 10: ")
checkNum = int(checkNum)
if checkNum % 10 == 0:
    print(f"Great news! {checkNum} is indeed a multiple of 10!")
else: 
    print(f"Awwwww, bummer. I hate to break it to you, but {checkNum} is not a multiple of 10.")