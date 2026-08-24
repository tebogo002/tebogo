first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: ")) 

full_name = (f"{first_name} {surname}")
print(f"\nWelcome, {full_name}!")
print(f"Uppercase: {full_name.upper()}")
print(f"Title Case: {full_name.title()}")

age_in_months = age * 12
print(f"Age in Months: {age_in_months}")

rounded_number = round(favourite_number, 2)
print(f"Favourite Number (rounded to 2 decimal places): {rounded_number}")

print("\nData Types:")
print(f"First Name: {type(first_name)}")
print(f"Surname: {type(surname)}") 
print(f"Age: {type(age)}")
print(f"Favourite Number: {type(favourite_number)}")