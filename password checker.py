# My own password checker!#
# Step 1: Get User Inputpassword = input("Enter a password: ")
password = input("type a password to check how strong it is: ")
# Step 3: Check Password Strength
has_length = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in "!@#$%^&*" for char in password)

# Step 4: Evaluate Password Strength
if has_length and has_upper and has_lower and has_digit and has_special:
    print("Password is strong!")
elif has_length >= 8:
    print("Password is weak: It must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
elif has_length >= 6:
    print("Password is very weak: It must contain at least eight characters.")
else:
    print("Password is extremely weak: It must contain at least six characters.")

