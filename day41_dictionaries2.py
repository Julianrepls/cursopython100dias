
#//// E X E R C I S E

# Create a dictionary that stores the following information about a website: name, URL, description and a star rating (out of 5).
# Use a loop to output the names of the keys, ask the user to type in the details and store the input in the dictionary.
# Finally, output the whole dictionary (keys and values).

webSite = {"name": None, "url": None, "desc": None}

for name, value in webSite.items():
    webSite[name] = input(f"{name}: ")

print()

for name, value in webSite.items():
    print(f"{name}:{value}")
