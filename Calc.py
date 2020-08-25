c = input("What do you want? (+; -; *; /; %; **0.5; **2; **)\n")
d = ['+', '-', '*',  '/', '%', '**0.5', '**2', '**']
if c != d:
    print("Wrong condition")
    exit(0)
a = int(input("Enter number\n"))
if c == '**0.5':
    print (a ** .5)
    exit(0)
elif c == '**2':
    print (a ** 2)
    exit(0)
else:
    b = int(input("Enter second number\n"))
if c == '+':
    print(a + b)
elif c == '-':
    print (a - b)
elif c == '*':
    print (a * b)
elif c == '/':
    print (a / b)
elif c == '%':
    print (a % b)
elif c == '**':
    print (a ** b)
elif c != c:
    print("Wrong condition")