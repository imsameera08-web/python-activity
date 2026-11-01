print("===== PASSWORD VALIDATION =====")

password = input("Enter your password: ")

upper = 0
lower = 0
digit = 0

for ch in password:

    if ch >= 'A' and ch <= 'Z':
        upper = upper + 1

    elif ch >= 'a' and ch <= 'z':
        lower = lower + 1

    elif ch >= '0' and ch <= '9':
        digit = digit + 1

if len(password) >= 8 and len(password) <= 20 and upper > 0 and lower > 0 and digit > 0:
    print("Password is valid")
else:
    print("Password is invalid")
    print("Use 8 to 20 characters with uppercase, lowercase and a digit")
    