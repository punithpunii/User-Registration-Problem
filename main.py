import re
#UC-1 First name starts with Cap and has minimum 3 characters
pattern = r"^[A-Z][A-Za-z]{2,}$"
firstname = input("Enter the First Name:")
if re.match(pattern, firstname):
    print("Valid Firstname", firstname)
else:
    print("Invalid Firstname")