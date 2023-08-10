def factorial_r(x):
    if x == 0:
        return 0
    if x == 1:
        return 1

    return x * factorial_r(x - 1)


# don't touch below this line


def test(x):
    res = factorial_r(x)
    print(f"x: {x}")
    print(f"x!: {res}")
    print("====================================")


def main():
    for i in range(1, 15):
        test(i)


main()
