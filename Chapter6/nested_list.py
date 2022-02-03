rivers = {
    'Amazon':['Brazil', 'Bolivia', 'Peru', 'Ecuador', 'Colombia', 'Venezuela', 'Guyana', 'Suriname', 'French Guiana'],
    'Rhine':['Germany', 'France', 'Switzerland', 'The Netherlands', 'Austria', 'Liechtenstein'],
    'Yangtze':'China'
    }
for riv, nations in rivers.items():
    if type(nations)==list:
        print(f"\nThe {riv.title()} river runs through: ")
        for nation in nations:
            print("\t\t\t\t",nation)
    else:    
        print(f"\nThe {riv.title()} river runs through {nations.title()}")