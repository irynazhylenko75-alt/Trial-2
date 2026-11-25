username = input("Enter username: ")
email = input("Enter email: ")
age = input("Enter age: ")
password = input("Create password: ")

errors = []


if len(username) < 5:
    errors.append("Username: must contain at least 5 characters")
if username and username[0].isdigit():
    errors.append("Username: must not start with a digit")
if " " in username:
    errors.append("Username: must not contain spaces")


if email.count("@") != 1:
    errors.append('Email: must contain exactly one "@"')


if not age.isdigit():
    errors.append("Age: must contain only digits")
elif int(age) < 16:
    errors.append("Age: must be at least 16")


if len(password) < 8:
    errors.append("Password: must contain at least 8 characters")
if " " in password:
    errors.append("Password: must not contain spaces")
if len(set(password)) == 1:
    errors.append("Password: must not consist of one repeated character. Try to be more creative")


if not errors:
    print("Data is valid")
else:
    print("Data is not valid")
    for error in errors:
        print(error)
  
