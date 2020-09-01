def calc(symbol: str, first: str, second: str):
    if first.isdigit() and second.isdigit():
        first = int(first)
        second = int(second)
    else:
        return None

    return {
        "+": first + second,
        "-": first - second,
        "*": first * second,
        "/": first / second,
        "%": first % second,
        "**": first ** second,
    }[symbol]


while True:
    operation = calc(
        input("What do you want? (+; -; *; /; %; **0.5; **2; **)\n"),
        input("Enter number:\t"),
        input("Enter number:\t"),
    )
    if not operation:
        print("Try again!")
    else:
        print(f"Great! \nYour result is:\t{operation}")

    final_ask = input("Want to continue?: Yes/No\t")
    if final_ask == "Yes":
        print("Okay Bro")
    elif final_ask == "No":
        print("Okay Bro")
        break
