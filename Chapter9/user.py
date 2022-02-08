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