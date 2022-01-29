instruments = ["xylophone", "french horn", "synthesizer", "bassoon"]
print("Original instrument list:", instruments)
instruments.append("oboe")
instruments.insert(2,"harmonium")
print("List with additions:", instruments)
del instruments[0]
instruments.remove("french horn")
instruments.pop()
print("List after deletions:", instruments)
print("List with temporary sort:", sorted(instruments))
instruments.reverse()
print("List sorted in reverse:", instruments)
instruments.sort()
print("List sorted alphabetically:", instruments)
counter = f"There are {len(instruments)} instruments in the final list."
print(counter)