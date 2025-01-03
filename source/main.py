import re
#UC-9 Implemented pytest

class InvalidName(Exception):
    pass

class InvalidEmail(Exception):
    pass

class InvalidPhno(Exception):
    pass

class InvalidPassword(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

def valid_name_check(name): # Name Validation
    name_pattern = r"^[A-Z][A-Za-z]{2,}$"
    if not re.match(name_pattern, name):
        raise InvalidName("Invalid Name,Name should start with UpperCase and has Alteast 3 Characters")
    return f"Valid Name {name}"

def valid_email_check(email): # Email Validation
    email_pattern = r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]*)?@[a-zA-Z]+\.[a-z]{2,}(\.[a-z]+)?$"
    if not re.match(email_pattern, email):
        raise InvalidEmail("Invalid Email Address, valid email-> (E.g. abc.xyz@bl.co.in)")
    return f"Valid Email Address {email}"
    
def valid_phno_check(phno): # Phno Validation
    phno_pattern = r"^[0-9]{2} [0-9]{10}" 
    if not re.match(phno_pattern, phno):
        raise InvalidPhno("Invalid Phone Number, valid Phone Number-> (E.g. 91 9919819801)")
    return f"Valid Phone Number {phno}"

def valid_passwd_check(password): # Password Validation
    passwd_pattern = r"(?=.*[A-Z])(?=.*[0-9]).{8,}$"
    if not (re.match(passwd_pattern, password) and len(re.findall(r"[!@#$%^&*()_+]", password)) == 1):
        raise InvalidPassword("Password must be at least 8 characters long, Atleast 1 Upper Case, Atleast 1 Number and Exactly 1 Special Character")
    return "Valid Password"
try:
    firstname = input("Enter the First Name:")
    print(valid_name_check(firstname)) #UC-1 First name starts with Cap and has minimum 3 characters
    lastname = input("Enter the Last Name:")
    print(valid_name_check(lastname)) #UC-2 Last name starts with Cap and has minimum 3 characters
    email = input("Enter your Email Address:")
    print(valid_email_check(email)) #UC-3 A User need to enter a valid email (E.g. abc.xyz@bl.co.in)
    phno = input("Enter your Phone Number:")
    print(valid_phno_check(phno)) #UC-4 A User need to follow pre-defined Mobile Format
    password = input("Enter your Password:")
    print(valid_passwd_check(password))
except InvalidName as e :
    print(e)
except InvalidEmail as e :
    print(e)
except InvalidPhno as e :
    print(e)
except InvalidPassword as e:
    print(e)