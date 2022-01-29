print("------------Original Barnyard----------")
barnyard = ["cow","pig","guinea hen","chicken","duck","quail"]
for critter in barnyard:
    print(critter)
farm = barnyard[:]
farm.append("turkey")
farm.append("goat")
farm.append("sheep")
farm.append("velociraptor")
print("------------Barnyard 2.0----------")
for resident in farm:
    print(resident)
print(f"The first three animals in Barnyard 2.0 are: {farm[0:3],}")
print(f"The middle three animals in Barnyard 2.0 are: {farm[4:7],}")
print(f"The last three animals in Barnyard 2.0 are: {farm[7:10]}")