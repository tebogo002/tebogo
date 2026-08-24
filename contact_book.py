contacts = []

# Adding a contact to phonebook
def add_contact():
    name = input("Enter the contact Name: ")
    phone = input("Enter the contact Phone Number: ")
    email = input("Enter the contact Email Address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})
    print(f"New Contact Added successfully!\nName: {name}\nPhone: {phone}\nEmail: {email}\n")


# Searching for a contact by name
def search_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Contact Found!\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\n")
            return contact
    print(f"No contact found with the name '{name}'.\n")
    return None


# Deleting a contact
def delete_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully!\n")
            return True
    print(f"No contact found with the name '{name}'.\n")
    return False


# View all contacts
def view_all():
    if not contacts:
        print("No contacts saved yet.\n")
        return
    print("\n----- All Contacts -----")
    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("-------------------------")
    print()


print("Welcome to the PhoneBook\n")

while True:
    menu = input("Select:\n1. To add a contact\n2. To search for a contact\n3. To delete a contact\n4. To view all your contacts\n5. To Exit\n")

    if menu == "1":
        add_contact()
    elif menu == "2":
        name = input("Enter the name to search for: ")
        search_contact(name)
    elif menu == "3":
        name = input("Enter the name of the contact to delete: ")
        delete_contact(name)
    elif menu == "4":
        view_all()
    elif menu == "5":
        print("Thank you for using the PhoneBook")
        break
    else:
        print("Incorrect option, please select the appropriate option\n")