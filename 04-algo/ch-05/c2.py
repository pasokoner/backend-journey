def num_countries_in_days(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1

    while time_in_country <= time_left:
        count += 1

        time_in_country = factor * time_in_country

        time_left = time_left - time_in_country

    return count


# don't touch below this line


def test(max_days, factor):
    countries_visited = num_countries_in_days(max_days, factor)
    print(f"- Max days: {max_days}")
    print(f"- Time factor: {factor}")
    print(f"Countries visited: {countries_visited}")
    print("=====================================")


def main():
    test(2, 1.2)
    test(3, 1.2)
    test(10, 1.2)
    test(100, 1.2)
    test(200, 1.2)
    test(1000, 1.3)


main()
