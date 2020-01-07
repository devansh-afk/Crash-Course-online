filename = 'text_files/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

file2name = 'text_files/pi_1000k.txt'
with open(file2name) as file2_object:
    lines2 = file2_object.readlines()

pi_string2 = ''
for line2 in lines2:
    pi_string2 += line2.rstrip()

print(f"{pi_string2[:52]}")


