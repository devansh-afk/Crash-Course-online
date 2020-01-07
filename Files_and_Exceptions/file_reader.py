with open('text_files/pi_digits.txt') as file_object:               # with closes the file after executing indented code
    contents = file_object.read()
print(contents)

# OR

"""file_object = open('pi_digits.txt')
contents = file_object.read()
print(contents)
file_object.close()
"""
file_name = 'text_files/pi_digits.txt'

with open(file_name) as file_object2:
    for line in file_object2:
        print(line.rstrip())

