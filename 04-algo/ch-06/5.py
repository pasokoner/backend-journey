import time
import random


def merge_sort(nums):
    if len(nums) < 2:
        return nums

    middle = len(nums) // 2

    return merge(merge_sort(nums[0:middle]), merge_sort(nums[middle:]))


def merge(first, second):
    final = []

    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1

    final.extend(second[j:])
    final.extend(first[i:])
    print(second[j:])
    print(first[i:])

    return final


# don't touch below this line


def benchmark(nums, show_nums):
    start = time.time()
    test(nums, show_nums)
    end = time.time()

    timeout = 1.00

    if (end - start) < timeout:
        print(f"test completed in less than {timeout * 1000} milliseconds!")
    else:
        print(f"test took too long ({(end - start) * 1000} milliseconds). Speed it up!")
    print("====================================")


def test(nums, show_nums):
    res = merge_sort(nums.copy())
    if show_nums:
        print(f"nums: {nums}")
        print(f"sorted: {res}")
    else:
        print(f"len nums: {len(nums)}")
        print(f"len sorted: {len(res)}")
    print("------------------------------------")


def main():
    benchmark(get_nums(10), True)
    benchmark(get_nums(100), True)
    benchmark(get_nums(1000), False)
    benchmark(get_nums(10000), False)


def get_nums(num):
    nums = []
    random.seed(1)
    for i in range(num):
        nums.append(random.randint(0, len(nums)))
    return nums


main()
