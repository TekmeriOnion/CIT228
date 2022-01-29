print("-----------Exercise 5-8-------------")
users = ["Jamaal","Paolo","Suz","Barb","admin"]
admin_greet = "Hello admin, would you like to see a status report?"
for user in users:
    if user == "admin":
        print(admin_greet)
    else:
        print(f"Hello {user}, glad to have you back on the site!")

print("-----------Exercise 5-9-------------")
users = []
admin_greet = "Hello admin, would you like to see a status report?"
if users:
    for user in users:
        if user == "admin":
            print(admin_greet)
        else:
            print(f"Hello {user}, glad to have you back on the site!")
else:
    print("We need to find some users!")
