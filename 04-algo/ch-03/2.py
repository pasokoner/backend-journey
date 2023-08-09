def find_max(nums):
    max = float("-inf")

    for num in nums:
        if num > max:
            max = num
    return max


# don't touch below this line


def test(nums):
    res = find_max(nums)
    print(f"- nums: {nums}")
    print(f"Max: {res}")
    print("====================================")


def main():
    test([7, 4, 3, 100, 2343243, 343434, 1, 2, 32])
    test([12, 12, 12])
    test([10, 200, 3000, 5000, 4])


main()
