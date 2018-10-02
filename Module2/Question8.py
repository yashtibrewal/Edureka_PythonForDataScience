# 8.A website requires a user to input username and password to register.
# Write a program to check the validity of password given by user.
# Following are the criteria for checking password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length of transaction password: 6
# 6. Maximum length of transaction password: 12

password = input("Enter the password:\n")
condition = True
lowercase = False
digits = False
uppercase = False
special = False
length = len(password)
if 6 <= length <= 12:
    for letter in password:
        if letter.islower():
            lowercase = True
            continue
        if letter.isdigit():
            digits = True
            continue
        if letter.isupper():
            uppercase = True
            continue
        if letter in '$#@':
            special = True
            continue
    if not lowercase or not digits or not uppercase or not special:
        print("Invalid")
    else:
        print("Valid")
else:
    print("Invalid")
