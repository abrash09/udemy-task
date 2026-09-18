def password ():
    create = input("Enter password: ")
    if len(create) >= 8:
        return True
    else:
        return False
password()