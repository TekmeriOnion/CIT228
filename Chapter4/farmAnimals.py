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
print("The first three animals in Barnyard 2.0 are: ", farm[0],farm[1],farm[2])
print("The middle three animals in Barnyard 2.0 are: ", farm[4],farm[5],farm[6])
print("The last three animals in Barnyard 2.0 are: ", farm[-1],farm[-2],farm[-3])