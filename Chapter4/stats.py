import random
num = random.randrange(10,100)
pool = list(range(num))
print(pool)
print("Largest:",max(pool))
print("Smallest:",min(pool))
print("Total:",sum(pool))
print("Average:",sum(pool)/len(pool))