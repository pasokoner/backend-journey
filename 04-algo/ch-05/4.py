def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    grandparent = 0
    parent = 1
    current = n
    for i in range(2, n + 1):
        current = parent + grandparent
        grandparent = parent
        parent = current

    return current


# don't touch below this line


def test(n):
    res = fib(n)
    print(f"n: {n}")
    print(f"Fibonacci's {n}th number: {res}")
    print("====================================")


def main():
    # print(fib(2))
    # print(fib(10))
    # print(fib(20))
    # print(fib(40))
    # print(fib(80))
    # print(fib(160))
    test(7)


main()
