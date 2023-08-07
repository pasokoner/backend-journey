def find_missing_ids(first_ids, second_ids):
    first = {i for i in first_ids}
    second = {i for i in second_ids}

    # for item in second:
    #     if item in first:
    #         first.remove(item)

    # return first

    return first.difference(second)


# Don't touch below this line


def test(first_ids, second_ids):
    ids = sorted(find_missing_ids(first_ids, second_ids))
    print(f"Customers with these ids were only in the first list:")
    for id in ids:
        print(f"- {id}")
    print("---")


test([1, 1, 1, 2, 2, 2, 3], [1, 2])
test([1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 9, 10], [1, 2, 2, 3, 4, 5, 6, 7, 8])
test(
    [1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 15, 18],
    [1, 2, 2, 3, 4, 5, 6, 7, 8, 100, 101, 103],
)
