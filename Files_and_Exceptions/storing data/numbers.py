import json

numbers = [2, 4, 5, 7, 10]

filename = 'number.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

