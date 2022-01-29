current_users = ["Jamaal","Paolo","Suz","Barb","Mark"]
lower_users = []
for user in current_users:
    lower_users.append(user.lower())
new_users = ["Paolo","Suz","Hayden","Cal","Wanda"]
for user in new_users:
    if user.lower() in lower_users:
        print(f"The username {user} is taken - you'll have to enter a different one")
    else:
        print(f"Congratulations! The username {user} is available")