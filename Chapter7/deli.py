print("----------------Exercise 7-8------------------")

sandwich_orders = ['BLT', 'Cuban', 'Cuban', 'Grilled Cheese', 'Mediterranean Veggie', 'PB & Nutella', 'Grilled Cheese', 'PB & Nutella']
finished_sandwiches = []

while sandwich_orders:
    currentSammie = sandwich_orders.pop()
    print(f"Your {currentSammie} is ready for pickup!")
    finished_sandwiches.append(currentSammie)
print("----------Today's Ordered Sandwiches-------------")

for sammie in finished_sandwiches:
    print(sammie)

print("----------------Exercise 7-9------------------")
sandwich_orders = ['BLT', 'Cuban', 'Cuban', 'Grilled Cheese', 'Mediterranean Veggie', 'PB & Nutella', 'Grilled Cheese', 'PB & Nutella']
finished_sandwiches = []

sandwich_orders.insert(2, 'Pastrami')
sandwich_orders.insert(4, 'Pastrami')
sandwich_orders.insert(6, 'Pastrami')

print("I'm so sorry, the deli is out of pastrami!")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    currentSammie = sandwich_orders.pop()
    print(f"Your {currentSammie} is ready for pickup!")
    finished_sandwiches.append(currentSammie)
print("----------Today's Ordered Sandwiches-------------")

for sammie in finished_sandwiches:
    print(sammie)