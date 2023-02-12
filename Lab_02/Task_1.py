# Task 1

# For NameError:
try:
    a == 9
except NameError:
    print("You have a Name Error here")

# For ZeroDivisionError
try:
    9 / 0
except ZeroDivisionError:
    print("You have a Zero Division error here")

# For SyntaxError:
# This is commented since it will cause an error in Python otherwise and will not allow the rest of the code to run
# try:
#     if 1 == True
#         print('yes')
# except SyntaxError:
#     print('You have syntax error here')
#
#
# For IndentationError:
# This is commented since it will cause an error in Python otherwise and will not allow the rest of the code to run
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
    print("You have an Index Error here")

# For KeyError
try:
    test_dict = {'test': 1}
    print(test_dict['trytest'])
except KeyError:
    print("You have a Key Error here")

# For ImportError
try:
    import blabla
except ImportError:
    print("You have an Import Error here")

# For AttributeError
try:
    example = 2
    example.append(3)
except AttributeError:
    print("You have an Attribute Error here")

# For RuntimeError
# have no fckn idea how to call this error so far


