import re
#UC-7 Password Rule3 – Should have at least 1 numeric number

class InvalidName(Exception):
    pass

class InvalidEmail(Exception):
    pass

class InvalidPhno(Exception):
    pass

class InvalidPassword(Exception):
    pass

def valid_name_check(name): # Name Validation
    name_pattern = r"^[A-Z][A-Za-z]{2,}$"
    if not re.match(name_pattern, name):
        raise InvalidName("Invalid Name,Name should start with UpperCase and has Alteast 3 Characters")
    else:
        print("Valid Name",name)

def valid_email_check(email): # Email Validation
    email_pattern = r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]*)?@[a-zA-Z]+\.[a-z]{2,}(\.[a-z]+)?$"
    if not re.match(email_pattern, email):
        raise InvalidEmail("Invalid Email Address, valid email-> (E.g. abc.xyz@bl.co.in)")
    else:
        print("Valid Email Address", email)
    
def valid_phno_check(phno): # Phno Validation
    phno_pattern = r"^[0-9]{2} [0-9]{10}" 
    if not re.match(phno_pattern, phno):
        raise InvalidPhno("Invalid Phone Number, valid Phone Number-> (E.g. 91 9919819801)")
    else:
        print("Valid Phone Number", phno)

def valid_passwd_check(password): # Password Validation
    passwd_pattern = r"(?=.*[A-Z])(?=.*[0-9]).{8,}$"
    if not re.match(passwd_pattern, password) :
        raise InvalidPassword("Password must be at least 8 characters long, Atleast 1 Upper Case, Atleast 1 Number")
    else:
        print("Valid Password")
try:
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
except InvalidName as e :
    print(e)
except InvalidEmail as e :
    print(e)
except InvalidPhno as e :
    print(e)
except InvalidPassword as e:
    print(e)