def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num

    return max_so_far


# Don't touch below this line


def test(nums):
    max = find_max(nums)
    print(f"The max of {nums} is {max}")


test([1, 2, 3, 4, 5])
test([1, 2, 300, 4, 5])
test([1, 20, 3, 4, 5])
test([-1, 2, 3, 4, 5])
test([1, 2, 3, 21, 18])
test([])
