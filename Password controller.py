def password_controller(a):
    if len(a) >= 8:
        return True
    else:
        return False

passwords = ["sjhvbufh48","47gfe","874gbfy4gf"]

for password in passwords:
    result = password_controller(password)
    print(password,result)


