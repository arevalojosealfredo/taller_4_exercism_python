from string import ascii_uppercase


def rows(letter):
    n = ascii_uppercase.index(letter)
    return [
        "".join(ascii_uppercase[abs(x)] if abs(y) + abs(x) == n else " "
                for x in range(-n, n + 1)) for y in range(-n, n + 1)
    ]