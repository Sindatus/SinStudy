symbol_list = ["+", "-", "*", "/", "%", "**"]


def num_operation(calculation_location):
    def check(symbol, first_number, second_number):
        def symbol_checker(symb=symbol):

            if symb in symbol_list:
                return True
            print("We can't perform this action")

        def number_checker(numb1=first_number, numb2=second_number):

            if numb1.isdigit() and numb2.isdigit():
                return True
            print("You need input number ")

        if symbol_checker() and number_checker() == True:
            return calculation_location(symbol, first_number, second_number)

    return check
