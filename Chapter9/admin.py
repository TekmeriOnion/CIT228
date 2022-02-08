from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, age, city, email, permissions, marketing_recipient="Yes", login_attempts=0):
        super().__init__(first_name, last_name, age, city, email, marketing_recipient, login_attempts)
        self.privileges = Privileges(permissions)