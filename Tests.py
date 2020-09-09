# def a(z):
#     symbol_list = ["+", "-", "*", "/", "%", "**", "!", "(", ")", "="]
#     spis_symbol = []
#     spis_number = []
#     for i in z:
#         if i in symbol_list:
#             spis_symbol.append(i)
#         elif i == ' ':
#             None
#         else:
#             spis_number.append(i)
#     return print(spis_symbol, spis_number)
#
# a(list(input()))

# def a(*z):
#     for i in z:
#         if i == ' ':
#             None
#         else:
#             i = int(i)
#             if i > 5:
#                 print(f"{i} \t more than 5")
#             else:
#                 print(f"{i} \t less than 5")
#     return a()
#
# a(list(input()))


# def a(*z):
#     print(z)
# a(list(input()))

# def a(z=15, t=20):
#     q(z, t)
#
#
# def q(z, t):
#     result = z + t
#     return print(result)
#
#
# a()


# ---------------------------------------------------------------------------------------------------------


# safety Calc.py

# def calc(symbol: str, first: str, second: str):
#     def check(a, b, c):
#         def symbol_ckeck(symb):
#             symbol_list = ["+", "-", "*", "/", "%", "**"]
#             if symb in symbol_list:
#                 return symb
#             else:
#                 print("We can't perform this action")
#                 return
#
#         if b.isdigit() and c.isdigit():
#             b = int(b)
#             c = int(c)
#         else:
#             print("You net input number ")
#             return
#
#         symbol_dictionary = {
#             "+": b + c,
#             "-": b - c,
#             "*": b * c,
#             "/": b / c,
#             "%": b % c,
#             "**": b ** c,
#         }
#         return symbol_dictionary[a] if symbol_ckeck(a) else None
#
#     return check(symbol, first, second)
#
#
# def main():
#     while True:
#         operation = calc(
#             input("What do you want? (+; -; *; /; %; **0.5; **2; **)\n"),
#             input("Enter number:\t"),
#             input("Enter number:\t"),
#         )
#         if not operation:
#             print("Try again!")
#         else:
#             print(f"Great! \nYour result is:\t{operation}")
#
#         final_ask = str.lower(input("Want to continue?: Yes/No\t"))
#         if final_ask == "yes":
#             print("Okay Bro")
#         elif final_ask == "no":
#             print("Okay Bro")
#             break
#
#
# main()


# #--------------------------------------------------------------------------------------------------------
#
#
# ########Sum_Calculation
# def sum(b, c):
#     return f"Результат сложения:\t {b + c}"
#
#
# def subtraction(b, c):
#     return f"Результат вычетания:\t {b + c * -1}"
#
#
# def multiply(b, c):
#     sum_number = int(b)
#     b = sum_number
#     c = int(c)
#     while c > 1:
#         c = c - 1
#         b = b + sum_number
#     return f"Результат умножения:\t {b}"
#
#
# def devide(b, c):
#     result = 0
#     constant = b
#     if c == 0:
#         print("We can't do this operation, please try again")
#     else:
#         while c >= b:
#             b = b + constant
#             result = result + 1
#     return f"Результат деления:\t {result}"
#
#
# def degree(b, c):
#     b = int(b)
#     c = int(c)
#     constant_b = b
#     constant_multiply = b
#     cos_b = b
#     while c > 1:
#         c = c - 1
#         constant_multiply = constant_b
#         cos_b = b
#         while constant_multiply > 1:
#             constant_multiply = constant_multiply - 1
#             b = b + cos_b
#
#     return f"Результат возведения в степень:\t {b}"
#
#
# def total(a: str, b: str, c: str):
#     b = int(b)
#     c = int(c)
#     dictionary = {"+": sum, "-": subtraction, "*": multiply, "/": devide, "**": degree}
#     return dictionary[a](b, c)
#
#
# z = (total(input("sign:\t"), input("number 1:\t"), input("number 2:\t")))
# print(z)
#
#
# #___________________________________________________________________________________________________________

# def t(thing):
#     def i(ing):
#         def b(*args):
#             return ing(*args)
#
#         return b
#     return i
#
# @t("lel")
# def c(q, l, s):
#     s = q + l + s
#     return s
#
#
# # z = c(input())
# print(c(input(), input(), input()))


# class Person:
#     engine = "unity"
#     work = "programmer"
#     justfor = 5
#     def bimb(self, a, b):
#         self.a = a
#         self.b = b
#         accaunt = {'name':self.a, 'balance': self.b}
#
# Juny = Person
# print(Juny.bimb('Jun', 10000))

a = (input("yes/no"))
x = a.lower()
print(x)