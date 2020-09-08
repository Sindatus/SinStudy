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