import sys
import string
from random import *

'''Iterate number of passwords and generate random numberOfPasswords passwords'''

numberOfPasswords = input('Enter the number of passwords you need: \'\n')

# Test if user input is convertible to integer
try:
    int(numberOfPasswords)
    print('You requested ' + numberOfPasswords + ' passwords. \'\n')
except ValueError:
    print('I\'im sorry but that\'s not a valid integer \'\n')
    sys.exit()

# create string with all letters (lowercase/uppercase) and digits
allchar = string.ascii_letters + string.digits
# print (allchar)

# a.join(sequence) uses a as separator for the characters composing sequence string
print('Passwords list \'\n')
for i in range(0, int(numberOfPasswords)):
    password = "".join(choice(allchar) for x in range(randint(6, 6)))
    print(password)
