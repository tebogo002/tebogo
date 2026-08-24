contacts = {
    "Tebogo": "123-456-7890", 
    "Palesa": "098-765-4321",
    "Neo": "555-555-5555" 
}

name = input("Enter the name to search for: ")

if name in contacts:
    print(f"Contact Found! {name}'s phone number is {contacts[name]}.") 
else:
    print("Contact not found.")