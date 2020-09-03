# Reading files
from sys import argv

# as an arg we should give a name of file
script, filename = argv

# then open a file and save it as object
txt = open(filename)

print(f"Here is your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())
