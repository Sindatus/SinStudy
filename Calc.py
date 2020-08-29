import flake8
import black


def calc(symbol, first, second):
    return {
        "+": first + second,
        "-": first - second,
        "*": first * second,
        "/": first / second,
        "%": first % second,
        "**": first ** second,
    }[symbol]


while True:
    mechanics = calc(
        input("What do you want? (+; -; *; /; %; **0.5; **2; **)\n"),
        int(input("Enter number:\t")),
        int(input("Enter number:\t")),
    )
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
        break
