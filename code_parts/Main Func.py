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