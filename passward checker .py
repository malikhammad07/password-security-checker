# +------------------------------+
# |  PASSWORD SECURITY CHECKER   |
# +------------------------------+

password = input("Enter password: ")

has_uppercase = False
for char in password:
    if char.isupper():
        has_uppercase = True
        break

if has_uppercase:
    print("Password has an uppercase letter:", has_uppercase)
else:
    print("Password does not have an uppercase letter:", has_uppercase)

has_lowercase = False
for char in password:
    if char.islower():
        has_lowercase = True
        break
if has_lowercase:
    print("Password has a lowercase Letter:", has_lowercase)
else:
    print("Password does not have a lowercase letter:", has_lowercase)

has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
        break

if has_digit:
    print("Password has a digit:", has_digit)
else:
    print("Password does not have a digit:", has_digit)

has_special_char = False
for char in password:
    if not char.isalnum():
        has_special_char = True
        break
if has_special_char:
        print("Password has a special character:",has_special_char)
else:
    print("Password does not have a special character:", has_special_char)

# Final comprehensive check
if len(password) >= 8 and has_uppercase and has_lowercase and has_digit and has_special_char:
    print("Password is strong")
elif len(password) < 8 and len(password) >= 5:
    print("Password is Medium")
else:
    print("Password is weak")