# Lab 01 Exercise 3: Secure Vault System

def validate_entry (name,pin):
    if (name == "Director" and pin == 1122) or (name =="Security" and pin == 9900):
        return print ("True")

    else:
        return print ("False")

validate_entry("Director",1122)
validate_entry("Director",9900)
validate_entry("director",1122)