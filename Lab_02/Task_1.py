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

# try:
#     if 1 == True
#         print('yes')
# except SyntaxError:
#     print('You have syntax error here')
#
#
# # # For IndentationError:
# try:
#     if 0 == False:
#     print('yes')
# except IndentationError:
#     print('You have an indentation error here')

# For IndexError
try:
    a = [0, 1]
    print(a[3])
except IndexError:
    print("You have an index error here")

# For KeyError


# For ImportError


# For AttributeError


# For RuntimeError


