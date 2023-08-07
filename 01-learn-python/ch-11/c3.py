def remove_nonints(nums):
    only_int = []
    for num in nums:
        if type(num) is int:
            only_int.append(num)

    return only_int


# Don't touch below this line


def test(nums):
    final = remove_nonints(nums)
    print(f"before: {nums}, after: {final}")


test(["200", 300, 2, False, "otherstring", 6])
test([True, 300, 2, False, "otherstring", 76, 86, "morestrings"])
test([300, 300, 2, False, "otherstring", 6, {}, 16])
test(["200", 300, 2, False, "something", 7, "something else"])
