def exponential_growth(n, factor, days):
    growth_sequence = []

    growth_sequence.append(n)

    for i in range(days - 1):
        new_growth = growth_sequence[-1] * factor

        growth_sequence.append(new_growth)

    return growth_sequence


# don't touch below this line


def test(n, factor, days):
    growth_sequence = exponential_growth(n, factor, days)
    print(f"- Initial followers: {n}")
    print(f"- Growth factor: {factor}")
    print(f"- Days: {days}")
    print(f"Growth sequence: {growth_sequence}")
    print("=====================================")


def main():
    test(10, 2, 4)
    test(20, 2, 6)
    test(30, 3, 3)
    test(40, 10, 10)


main()
