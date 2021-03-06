def square(number):
    if number <= 0 or number > 64:
        raise ValueError("error")

    return int(2 ** (number - 1))


def total():
    return sum(square(i) for i in range(1, 65))
