# Exercise 10-3
"""
name = (input("Please enter your full name: "))
with open("guest.txt","a") as guestFile:
    name += "\n"
    guestFile.write(name)
# Exercise 10-4
name = input("Please enter your full name (enter 'q' to quit): ")

with open("guest_book.txt","a") as guestFile:
    while name != "q":
        print(f"Hello {name}, welcome to the Inn!")
        name += "\n"
        guestFile.write(name)
        name = input("Please enter your full name (enter 'q' to quit): ")
"""
import os
import random

if os.path.exists("guest_book.txt"):
    os.remove('guest_book.txt')

guest = input("Please enter your full name (enter 'q' to quit): ")
occupiedRooms = []
with open('guest_book.txt','w') as guestFile:
    while guest != "q":
        roomNum = random.randint(1,50)
        while roomNum in occupiedRooms:
            roomNum = random.randint(1,50)
        occupiedRooms.append(roomNum)
        print(f"Hello {guest}, welcome to the Inn! You'll be in room {roomNum}")
        guest += f", Room #{roomNum}\n"
        guestFile.write(guest)
        guest = input("Please enter your full name (enter 'q' to quit): ")
with open("guest_book.txt") as guestBook:
    print("-------Room Assignments--------")
    for entry in guestBook:
        print(entry)