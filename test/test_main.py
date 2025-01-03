import pytest 
from source.main import valid_name_check,valid_email_check,valid_passwd_check,valid_phno_check,InvalidName,InvalidEmail,InvalidPhno,InvalidPassword

def test_valid_name():
    try:
        assert valid_name_check("punith") 
    except InvalidName as e:
        print(e)
        
def test_valid_email():
    assert valid_email_check("punith@gmail.com") == "Valid Email Address punith@gmail.com"
    with pytest.raises(InvalidEmail):
        valid_email_check("punithgmail")

def test_valid_phno():
    assert valid_phno_check("91 1234567890") == "Valid Phone Number 91 1234567890"
    with pytest.raises(InvalidPhno):
        valid_phno_check("9008007600")

def test_valid_passwd():
    assert valid_passwd_check("Tom00@hh") == "Valid Password"
    with pytest.raises(InvalidPassword):
        valid_passwd_check("tom12345")