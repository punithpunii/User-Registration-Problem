import re
#UC-3 A User need to enter a valid email (E.g. abc.xyz@bl.co.in)

def valid_name_check(name):
    name_pattern = r"^[A-Z][A-Za-z]{2,}$"
    if re.match(name_pattern, name):
        print("Valid Name", name)
    else:
        print("Invalid Name")
        exit()

def valid_email_check(email):
    email_pattern = r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]*)?@[a-zA-Z]+\.[a-z]{2,}(\.[a-z]+)?$"
    if re.match(email_pattern, email):
        print("Valid Email Address", email)
    else:
        print("Invalid Email Address, valid email-> (E.g. abc.xyz@bl.co.in)")
        exit()

firstname = input("Enter the First Name:")
valid_name_check(firstname) #UC-1 First name starts with Cap and has minimum 3 characters
lastname = input("Enter the Last Name:")
valid_name_check(lastname) #UC-2 Last name starts with Cap and has minimum 3 characters
email = input("Enter your Email Address:")
valid_email_check(email)
