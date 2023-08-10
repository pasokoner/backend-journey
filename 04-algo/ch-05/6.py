def power_set(input_set):
    if len(input_set) == 0:
        return [[]]

    subset = []

    result = power_set(input_set[1:])

    for sub in result:
        subset.append([input_set[0]] + sub)

    return subset + result


# don't touch below this line


def test(input_set):
    result = power_set(input_set)
    print(f"Number of subsets of {input_set}: {len(result)}")
    print("====================================")


def main():
    for i in range(1, 22):
        nums = list(range(1, i))
        test(nums)

    mylist = [0, 1, 2]
    print(mylist[3:])


main()
