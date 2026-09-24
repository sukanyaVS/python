# .Create a program that checks the strength of a password.
# Requirements:
# A password should contain:
# At least 8 characters
# At least one uppercase letter
# At least one lowercase letter
# At least one number
# At least one special character

password = input("Enter a password: ")
if len(password) < 8:
    print("Password must be at least 8 characters long.")
else:
    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special = False
    special_characters = "!@#$%^&*()-+"
    
    for char in password:
        if char.isupper():
            has_uppercase = True
        if char.islower():
            has_lowercase = True
        if char.isdigit():
            has_number = True
        if char in special_characters:
            has_special = True
    
    if has_uppercase and has_lowercase and has_number and has_special:
        print("Password is strong.")
    else:
        print("Password is not strong enough.")

        if not has_uppercase:
            print("Password must contain an uppercase letter.")

        if not has_lowercase:
            print("Password must contain a lowercase letter.")

        if not has_number:
            print("Password must contain a number.")

        if not has_special:
            print("Password must contain a special character.")