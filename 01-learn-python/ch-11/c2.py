def find_min(nums):
    min = float("+inf")

    for num in nums:
        if num < min:
            min = num

    return min


# Don't touch below this line


def test(nums):
    min = find_min(nums)
    print(f"min is {min}")


test([-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7])
test([4, 3, 2, 1, 18, 1, 2, 3, 4, 5, 6, 7])
test([43, 234, 65465, 234, 2343, 443, 2123, 8768])
test(
    [
        54,
        545,
        453,
        2,
        65,
        4,
        7,
        87,
        7,
        545,
        4,
        32,
        32,
        423,
        32,
        4,
        24,
        32,
        2,
        43,
        432,
        4,
        432,
        423,
        43,
        54,
        6,
        5,
        76,
        5787,
        67,
        876,
        876,
        3,
        54,
        4,
        4,
        3,
        3,
        24,
        2,
        43,
        4,
        324,
        42,
        423,
        34,
        8,
    ]
)
