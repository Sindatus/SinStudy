move = input("What do you want? (+; -; *; /; %; **0.5; **2; **)\n")
_array = ['+', '-', '*', '/', '%', '**0.5', '**2', '**']

if move in _array:
    print("")
else:
    print("Wrong condition")
    exit(0)

first_number = int(input("Enter number\n"))

if move == '**0.5':
    print(first_number ** .5)
    exit(0)
elif move == '**2':
    print(first_number ** 2)
    exit(0)
else:
    second_number = int(input("Enter second number\n"))
if move == '+':
    print(first_number + second_number)
elif move == '-':
    print(first_number - second_number)
elif move == '*':
    print(first_number * second_number)
elif move == '/':
    print(first_number / second_number)
elif move == '%':
    print(first_number % second_number)
elif move == '**':
    print(first_number ** second_number)
