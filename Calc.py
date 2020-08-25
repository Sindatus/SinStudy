
c = input("What do you want? (+; -; *; /; %; **0.5; **2; **)\n")
a = int(input("Enter number\n"))
if c == '**0.5':
    print (a ** .5)
    SystemExit
elif c == '**2':
    print (a ** 2)
    SystemExit
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
