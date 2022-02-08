class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print(f"This account has the following permissions:")
        for priv in self.privileges:
            print(priv)