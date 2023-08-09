def remove_duplicates(nums):
    unique_follower = []
    for num in nums:
        if num not in unique_follower:
            unique_follower.append(num)

    return unique_follower


# don't touch below this line


def test(nums):
    result = remove_duplicates(nums)
    print(f"Original list: {nums}")
    print(f"List after removing duplicates: {result}")
    print("====================================")


def main():
    test([1, 2, 3, 4, 4, 5, 6, 7, 7, 7])
    test([10, 10, 20, 30, 30, 30, 40, 50, 50])
    test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


main()
