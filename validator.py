"""Create a data validation module with custom exceptions: InvalidEmailError, 
   InvalidAgeError, EmptyFieldError. Add regex-based email validation and a full test 
   suite using pytest."""

import re

class InvalidEmailError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class EmptyFieldError(Exception):
    pass

EMAIL_PATTERN = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

def validate_email(email:str):
    if not email:
        raise EmptyFieldError("Email cannot be empty")
    if not EMAIL_PATTERN.match(email):
        raise InvalidEmailError("Invalid Email Error")
    return True

def validate_age(age:int):
    if age is None:
        raise EmptyFieldError("Age cannot be empty")
    if not isinstance(age,int) or age<0 or age>120:
        raise InvalidAgeError("Age must be between 0 and 120")
    return True

def validate_user(email:str,age:int):
    validate_email(email)
    validate_age(age)
    return True
    