print("-----------------------------------------")
print("Exercise 1")
name="nicco pandolfi"
print(name.title())
print(name.upper())
print(name.lower())
print("My first initial is: ",name[0].upper())

print("-----------------------------------------")
print("Exercise 2")
noun = "magician"
adj = "tall"
verb = "disappointed"
ending = "his audience."
sentence1 = "the " + adj + " " + "skeletal " + noun + " " + verb + " " + ending
sentence2 = f"the {adj} skeletal {noun} {verb} {ending}"
print(sentence1.upper())
print(sentence2.lower())

print("-----------------------------------------")
print("Exercise 3\n")
wcw_poem = """I have eaten
the plums
that were in
the icebox

and which
you were probably
saving
for breakfast

Forgive me
they were delicious
so sweet 
and so cold"""
print(wcw_poem + "\n")

print("-----------------------------------------")
print("Exercise 4\n")
weather1, weather2, weather3 = "foggy", "icy", "misty"
land1, land2, land3 = "creekbed", "mountain", "mesa"
print("Weather\t\tLandscape\n")
print(weather1 + "\t\t" + land1 + "\n")
print(weather2 + "\t\t" + land2 + "\n")
print(weather3 + "\t\t" + land3 + "\n")
