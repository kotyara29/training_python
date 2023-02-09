# Task 1

# For NameError:
try:
    a == 9
except NameError:
    print("You have a name error here")

# For ZeroDivisionError
try:
    9 / 0
except ZeroDivisionError:
    print("You have a zero division error here")

# For SyntaxError:

try:
    if 1 == True
        print('yes')
except SyntaxError:
    print('You have syntax error here')


