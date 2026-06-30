inp = input("Enter any character or number")
t = ord(inp)
if len(inp) == 1:
    print("ASCII value:", t)
    if 65 <= t <= 90:
        print("This is an uppercase letter")
    elif 97 <= t <= 122:
        print("This is a lowercase letter")
    elif 48 <= t <= 57:
        print("This is a digit")
    elif t == 32:
        print("This is a space character")
    else:
        print("This is a special character")
else:
    print("Please enter only one character")
