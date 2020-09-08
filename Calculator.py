def qwiz(calculation_location):
    def check(symbol, first_number, second_number):

        def symbol_check(symb=symbol):

            symbol_list = ["+", "-", "*", "/", "%", "**"]
            if symb in symbol_list:
                return True
            else:
                print("We can't perform this action")
                return

        def number_check(numb1=first_number, numb2=second_number):

            if numb1.isdigit() and numb2.isdigit():
                numb1 = int(numb1)
                numb1 = int(numb2)
                return True
            else:
                print("You need input number ")
                return

        if symbol_check() and number_check() == True:
            return calculation_location(symbol, first_number, second_number)
        else:
            return None

    return check


@qwiz
def calculation(symbol: str, first: str, second: str):
    first = int(first)
    second = int(second)
    symbol_dictionary = {
        "+": first + second,
        "-": first - second,
        "*": first * second,
        "/": first / second,
        "%": first % second,
        "**": first ** second,
    }
    return symbol_dictionary[symbol]


def main():
    while True:
        operation = calculation(
            input("What do you want? (+; -; *; /; %; **0.5; **2; **)\n"),
            input("Enter number:\t"),
            input("Enter number:\t"),
        )

        if not operation:
            print("Try again!")
        else:
            print(f"Great! \nYour result is:\t{operation}")

        final_ask = str.lower(input("Want to continue?: Yes/No\t"))
        if final_ask == "yes":
            print("Okay Bro")
        elif final_ask == "no":
            print("Okay Bro")
            break


main()
