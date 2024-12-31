import re
#UC-5 Password Rule1 – minimum 8 Characters

def valid_name_check(name): # Name Validation
    name_pattern = r"^[A-Z][A-Za-z]{2,}$"
    if re.match(name_pattern, name):
        print("Valid Name", name)
    else:
        print("Invalid Name")
        exit()

def valid_email_check(email): # Email Validation
    email_pattern = r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]*)?@[a-zA-Z]+\.[a-z]{2,}(\.[a-z]+)?$"
    if re.match(email_pattern, email):
        print("Valid Email Address", email)
    else:
        print("Invalid Email Address, valid email-> (E.g. abc.xyz@bl.co.in)")
        exit()
    
def valid_phno_check(phno): # Phno Validation
    phno_pattern = r"^[0-9]{2} [0-9]{10}" 
    if re.match(phno_pattern, phno):
        print("Valid Phone Number", phno)
    else:
        print("Invalid Phone Number, valid Phone Number-> (E.g. 91 9919819801)")
        exit()

def valid_passwd_check(password): # Passwd Validation
    passwd_pattern = r".{8,}"
    if re.match(passwd_pattern, password):
        print("Valid Password")
    else:
        print("Invalid Password, valid Phone Number-> (E.g. 91 9919819801)")
        exit()

firstname = input("Enter the First Name:")
valid_name_check(firstname) #UC-1 First name starts with Cap and has minimum 3 characters
lastname = input("Enter the Last Name:")
valid_name_check(lastname) #UC-2 Last name starts with Cap and has minimum 3 characters
email = input("Enter your Email Address:")
valid_email_check(email) #UC-3 A User need to enter a valid email (E.g. abc.xyz@bl.co.in)
phno = input("Enter your Phone Number:")
valid_phno_check(phno) #UC-4 A User need to follow pre-defined Mobile Format
password = input("Enter your Password:")
valid_passwd_check(password)