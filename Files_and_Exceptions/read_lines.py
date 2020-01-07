filename = 'text_files/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()       # Use readline() to read the first line and put the limit in the brackets.

for line in lines:
    print(line.rstrip())

