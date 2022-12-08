a = 11
b = 9


if a % 2 == 0 and b % 2 == 0 or a % 2 == 1 and b % 2 == 1:
    print("True")
else:
    print("False")


password = "soasasdasdasdasd"

if len(password) >= 8 and "@" in password or "#" in password:
    print("Password is strong")
else:
    print("Password is weak")

print(ord('Z'))
print(chr(88))