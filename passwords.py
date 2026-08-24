# Users often forget their passwords. 
# Create a script that helps them by showing a secure hint.
# 1.Ask the user to input their secret password.
# 2.Use .strip() to clean up any accidental spaces they might have typed at the start or end.
# 3.Grab the very first letter and the very last letter of the passwords using string indexing. 
# 4.Print a hint using an f-string that forces the letters into uppercase so they stand out. (e.g., “Your password hint: It starts with P and ends with N”).

password = input("Enter your password: ").strip()

print (f"Your password hint: It starts with a {password[0].upper()} and ends with a {password[-1].upper()}")
