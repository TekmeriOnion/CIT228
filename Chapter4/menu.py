print("-----------Menu-----------")
menu = ("omelet","pancakes","parfait","waffles","huevos rancheros")
for dish in menu:
    print(dish)
print("-----------Updated Menu-----------")
## menu[2] = "smoothie" caused an error b/c tuples don't support item assignment
menu = ("omelet","pancakes","smoothie","crepes","huevos rancheros")
for dish in menu:
    print(dish)