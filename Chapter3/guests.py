print("----------Exercise 3-4----------------")
guests = ["Mark Twain", "Jacinda Ardern", "John Lennon"]
invite = ", are you available for a dinner party on Friday?"
print(guests[0], invite)
print(guests[1], invite)
print(guests[2], invite)
print("----------Exercise 3-5----------------")
print(guests[0], " sadly has a prior commitment and cannot join us.")
guests[0] = "Jesse Ball"
print(guests[0], invite)
print(guests[1], invite)
print(guests[2], invite)
print("----------Exercise 3-6----------------")
print("Our new dining table comes Thursday!")
guests.insert(0,"Gandalf the Grey")
guests.insert(2, "Esperanza Spalding")
guests.append("Kurt Vonnegut")
print("I can now invite",len(guests),"guests to dinner.")
print(guests[0], invite)
print(guests[1], invite)
print(guests[2], invite)
print(guests[3], invite)
print(guests[4], invite)
print(guests[5], invite)
print("----------Exercise 3-7----------------")
print("Table delivery has been postponed - curse the supply chain! Now we can only host two for dinner Friday.")
uninvited = guests.pop()
disinvite = ", so sorry but we'll have to get together another time."
print(uninvited, disinvite)
uninvited = guests.pop()
disinvite = ", so sorry but we'll have to get together another time."
print(uninvited, disinvite)
uninvited = guests.pop()
disinvite = ", so sorry but we'll have to get together another time."
print(uninvited, disinvite)
uninvited = guests.pop()
disinvite = ", so sorry but we'll have to get together another time."
print(uninvited, disinvite)
confirmation = "we are still on for dinner on Friday - see you then!"
print(guests[0], confirmation)
print(guests[1], confirmation)
del guests[1], guests[0]
print(guests)
