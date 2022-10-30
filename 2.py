a = {}
while True:
    username_duplicate = bool
    while True:
        username = input("Username: ")
        for name, info in a.items():
            if name == username:
                username_duplicate = True
            else:
                username_duplicate = False
        if username_duplicate is True:
            print("Username unavailable. Please enter again")
        else:
            break
    while True:
        password = input("Password: ")
        if 6 <= len(password) <= 12:
            break
        else:
            print("Password must be between 6 and 12 characters. Please enter again")
            continue
    salary = input("Salary: ")
    email_duplicate = bool
    while True:
        email = input("Email: ")
        for name, info in a.items():
            if a.get(name).get("Email") == email:
                email_duplicate = True
            else:
                email_duplicate = False
        if email_duplicate is True:
            print("Email unavailable. Please enter again")
        else:
            a.update({username: {"Password": password, "Salary": salary, "Email": email}})
            break
    cont = input("Do you want to continue? ")
    if cont.lower() == "yes":
        continue
    else:
        break
for name,info in a.items():
    print()
    print(f'Username: {name}')
    for key in info:
        print(f'{key}: {info.get(key)}')
print("\nHave a nice day")