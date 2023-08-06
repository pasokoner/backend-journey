import math


def is_prime(number):
    if number <= 1:
        return False
    else:
        for i in range(2, math.floor(math.sqrt(number)) + 1):
            if (number % i) == 0:
                return False

    return True


# Don't touch below this line

for i in range(0, 25):
    print(f"{i} is prime: {is_prime(i)}")
