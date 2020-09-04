from sys import argv
from os.path import exists

# unpack 2 files
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#save file in object, read it and assign to another object
in_file = open(from_file)
indata = in_file.read()
print(type(indata))

# calculate amount of bytes
print(f"The input file is {len(indata)} bytes long")

# check if file to write exists
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# open file to read and write to in_file
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()
