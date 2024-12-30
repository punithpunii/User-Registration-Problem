import re
#UC-2 Last name starts with Cap and has minimum 3 characters

def valid_name_check(name):
    name_pattern = r"^[A-Z][A-Za-z]{2,}$"
    if re.match(name_pattern, name):
        print("Valid Name", name)
    else:
        print("Invalid Name")
        exit()

firstname = input("Enter the First Name:")
valid_name_check(firstname) #UC-1 First name starts with Cap and has minimum 3 characters
lastname = input("Enter the Last Name:")
valid_name_check(lastname) #UC-2 Last name starts with Cap and has minimum 3 characters
