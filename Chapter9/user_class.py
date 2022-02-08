print("=================Exercise 9-3===================")
class User:
    def __init__(self, first_name, last_name, age, city, email, marketing_recipient="Yes", login_attempts=0):
        """Initialize new user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.city = city
        self.email = email.strip()
        self.marketing_recipient = marketing_recipient
        self.login_attempts = int(login_attempts)

    def describe_user(self):
        """Return list view of user details"""
        print(f"""
        User Summary
        --------------
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Age: {self.age}
        City = {self.city}
        Email = {self.email}
        Marketing Recipient? = {self.marketing_recipient}
        """)
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()}, good to see you back on the site!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        
users =[]
user1 = User("Rob", "Lazarro", "39", "Birmingham, AL", "robbie@madeup.net")
users.append(user1)
user2 = User("Sal", "Fosse", "52", "Flint, MI", "sal@madeup.net", "No")
users.append(user2)
user3 = User("Tess", "Winters", "41", "Boston, MA", "tessw@madeup.net")
users.append(user3)
user4 = User("Hollie", "Jones", "71", "Portland, ME", "hjones@madeup.net", "No")
users.append(user4)

for user in users:
    user.describe_user()
    user.greet_user()

print("=================Exercise 9-5===================")

user1.increment_login_attempts()
print(f"User {user1.first_name} {user1.last_name} has made {user1.login_attempts} login attempts")
user1.increment_login_attempts()
print(f"User {user1.first_name} {user1.last_name} has made {user1.login_attempts} login attempts")
user1.increment_login_attempts()
print(f"User {user1.first_name} {user1.last_name} has made {user1.login_attempts} login attempts")
user1.reset_login_attempts()
print(f"User {user1.first_name} {user1.last_name}'s login attempts have been reset.")
print(f"User {user1.first_name} {user1.last_name} has made {user1.login_attempts} login attempts")