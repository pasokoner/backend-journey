def divide_list(nums, divisor):
    return [num / divisor for num in nums]


# don't touch below this line


def test(nums, divisor):
    res = divide_list(nums, divisor)
    print(f"given nums={nums} and divisor={divisor}, {res} was returned")


test([6, 8, 10], 2)
test([9, 21, 333312], 3)
test([5, 25, 543664565], 5)
