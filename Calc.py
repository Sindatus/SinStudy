def calc(symbol, first, second):
    return {"+": first + second, "-": first - second, "*": first * second, "/": first / second, "%": first % second,
            "**": first ** second}[symbol]


cycle_control = True
while cycle_control:
    mechanics = calc(input("What do you want? (+; -; *; /; %; **0.5; **2; **)\n"), int(input("Enter number:\t")),
                     int(input("Enter number:\t")))
    if not mechanics:
        print("Try again!")
    else:
        print("Great")
        print(mechanics)

    final_ask = input("Want to continue?: Yes/No\t")
    if final_ask == "Yes":
        print("Okay Bro")
    elif final_ask == "No":
        print("Okay Bro")
        cycle_control = False
