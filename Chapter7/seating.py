partySize = input("How many people are in your party for dinner this evening? ")
partySize = int(partySize)
if partySize > 8:
    print("Please wait in the lobby or at the bar until your table is ready.")
else:
    print("Your table is ready, right this way!")