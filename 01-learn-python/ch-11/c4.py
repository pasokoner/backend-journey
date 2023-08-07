def factorial(num):
    if num == 0:
        return 0

    total = 1
    for i in range(1, num + 1):
        total *= i

    return total


# don't touch below this line


def test(num):
    fact = factorial(num)
    print(f"The factorial of {num} is {fact}")


test(0)
test(4)
test(5)
test(7)
test(9)
test(13)
test(15)
test(14)
