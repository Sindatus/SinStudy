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