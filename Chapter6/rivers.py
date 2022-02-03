rivers = {
    'Amazon':['Brazil', 'Bolivia', 'Peru', 'Ecuador', 'Colombia', 'Venezuela', 'Guyana', 'Suriname', 'French Guiana'],
    'Rhine':['Germany', 'France', 'Switzerland', 'The Netherlands', 'Austria', 'Liechtenstein'],
    'Yangtze':'China'
    }

for river,country in rivers.items():
    if type(country) == list:
        print(f"The {river} runs through {country}.")
    else:
        print(f"The {river} runs through {country}.")

print("\nThe rivers in my dictionary so far include:")
for river in rivers.keys():
    print(river)

print("\nThe countries in in my dictionary so far include:")
for country in rivers.values():
    if type(country) == list:
        for entry in country:
            print(entry)
    else:
        print(country)