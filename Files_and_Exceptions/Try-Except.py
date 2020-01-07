print("Give me 2 numbers. I'll divide them\nEnter \'q\' to quit. ")
while True:
    first_no = input('Enter first number')
    if first_no == 'q':
        break
    second_no = input("Enter second number")
    if second_no == 'q':
        break
    try:
        answer = int(first_no) / int(second_no)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(answer)

