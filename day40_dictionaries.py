# myUser = {"name":"David", "age": 128}

# myUser["age"] = 129

# print(myUser)


name = input("whats your name_ ").strip().capitalize()
age = input("How old are you?_ ").strip()
tlf = input("Telephone number_ ").strip()
email = input("Your email_ ").strip()
address = input("Your address_ ").strip()

contact = {"name": name, "age": age, "tlf": tlf, "email": email, "address": address}
print()

print(f"Name: {contact['name']}")
print(f"age: {contact['age']}")
print(f"tlf: {contact['tlf']}")
print(f"email: {contact['email']}")
print(f"address: {contact['address']}")

