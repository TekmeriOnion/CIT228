print("---------------Hands on 1---------------------")
grub = ['risotto', 'palak paneer', 'fish tacos', 'shakshuka', 'peanut butter milkshakes', 'homemade noodles']
print("Favorite foods: ", grub)
luckynum = [27, 3, 72, 137, 59, 229]
print("Lucky numbers: ", luckynum)
flix = ['Big Night', 'Rushmore', 'Parasite']
print("Favorite movies: ", flix)
combo = [grub[1], grub[4], luckynum[2], luckynum[5], flix[0], flix[2]]
print("Combo list: ", combo)
print("Last food item = ", grub[-1])
print("2nd, 4th, and 6th numbers = ", luckynum[1], " ", luckynum[3], " ", luckynum[5])
print("All movies = ", flix[0], " ", flix[1], " ", flix[2])
print("First food, number, and movie = ", combo[0], " ", combo[2], " ", combo[4])
print("---------------Hands on 2---------------------")
flix.append("Young Frankenstein")
print("Added movie: ",flix)
luckynum.insert(3, 87)
print("Added number at sub 3: ", luckynum)
grub.insert(5, "garlic")
print("Added food at sub 5: ", grub)
del grub[3]
print("Deleted grub[3]: ", grub)
luckynum.pop()
print("Deleted last number: ", luckynum)
luckynum.pop(2)
print("Deleted number at sub 2: ", luckynum)
print("---------------Hands on 3---------------------")
flix.sort()
print("Sorted movie list: ", flix)
grub.sort()
print("Sorted grub list: ", grub)
print("Temp sorted number list: ", sorted(luckynum))
print("Unsorted number list: ", luckynum)
flix.reverse()
print("Movies sorted in reverse: ", flix)