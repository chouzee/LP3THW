# argv is argument variable
from sys import argv
# in the line 4 we will unpack arguments
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is", second)
print("Your third variable is:", third)

