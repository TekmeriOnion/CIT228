print("=================Exercises 9-7 and 9-8===================")
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
        """greet an active user"""
        print(f"Hello {self.first_name.title()}, good to see you back on the site!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print(f"This account has the following permissions:")
        for priv in self.privileges:
            print(priv)

class Admin(User):
    def __init__(self, first_name, last_name, age, city, email, permissions, marketing_recipient="Yes", login_attempts=0):
        super().__init__(first_name, last_name, age, city, email, marketing_recipient, login_attempts)
        self.privileges = Privileges(permissions)
        
users =[]
user1 = User("Rob", "Lazarro", "39", "Birmingham, AL", "robbie@madeup.net")
users.append(user1)
user2 = User("Sal", "Fosse", "52", "Flint, MI", "sal@madeup.net", "No")
users.append(user2)
user3 = User("Tess", "Winters", "41", "Boston, MA", "tessw@madeup.net")
users.append(user3)
user4 = User("Hollie", "Jones", "71", "Portland, ME", "hjones@madeup.net", "No")
users.append(user4)

adminPowers = ["can add post","can delete post","can modify user info","can ban user","can view analytics"]
admin = Admin("Sacha","Sarver",37,"Minneapolis, MN","sacha@madeup.net",adminPowers)
users.append(admin)

admin.privileges.show_privileges()