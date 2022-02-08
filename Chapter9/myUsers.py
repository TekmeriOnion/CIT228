from user import User
from privileges import Privileges
from admin import Admin

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