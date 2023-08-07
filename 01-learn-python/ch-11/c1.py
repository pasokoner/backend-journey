def number_sum(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total


# Don't touch below this line


def test(n):
    sum = round(number_sum(n))
    print(f"The sum of 1->{n} is {sum}")


test(3)
test(5)
test(18)
test(227)
