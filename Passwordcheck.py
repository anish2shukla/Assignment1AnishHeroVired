import re

passwordInput=input("enter password")

def check_password_strength (passwordInput):
    if len(passwordInput)<8:
        print("Password length is less than 8.")
        return False
    if not re.search(r"[a-z]", passwordInput):
        print("Password does not contain lower case alphabets")
        return False
    if not re.search(r"[A-Z]", passwordInput):
        print("Password does not contain bigger case alphabets")
        return False
    if not re.search(r"[0-9]", passwordInput):
        print("Password does not contain digits")
        return False
    if not re.search(r"[!@#$%^&*()_+.]", passwordInput):
        print("Password does not contain Special characters")
        return False
    
    print(" Strong Password")
    return True
check_password_strength(passwordInput)