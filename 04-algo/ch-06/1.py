import random


def bubble_sort(nums):
    count = len(nums)
    while count > 0:
        for i in range(1, count):
            if nums[i - 1] > nums[i]:
                temp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = temp

        count -= 1

    return nums


# don't touch below this line


def test(nums):
    res = bubble_sort(nums.copy())
    print(f"nums: {nums}")
    print(f"sorted: {res}")
    print("====================================")


def main():
    test(get_nums(10))
    test(get_nums(100))
    test(get_nums(500))


def get_nums(num):
    nums = []
    random.seed(0)
    for i in range(num):
        nums.append(random.randint(0, len(nums)))
    return nums


main()
