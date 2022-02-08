from random import choice

class Die:
    def __init__(self, sides=6):
        self.sides = int(sides)
    
    def roll_die(self):
        outcomes = range(1,self.sides+1)
        print(choice(outcomes))

sixer = Die()
print(f"Now rolling a {sixer.sides}-sided die 10 times...")
for i in range(1,11):
    sixer.roll_die()

tenSider = Die(10)
print(f"Now rolling a {tenSider.sides}-sided die 10 times...")
for i in range(1,11):
    tenSider.roll_die()

nerdiest = Die(20)
print(f"Now rolling a {nerdiest.sides}-sided die 10 times...")
for i in range(1,11):
    nerdiest.roll_die()
