numbers = [
    0,
    99,
    2,
    33,
    61,
    44,
    9,
    10,
    12,
    240,
    35,
    9082,
    1234,
]
num_evens = 0
num_odds = 0

# Don't touch above this line

for num in numbers:
    if num & 1:
        num_odds += 1
    else:
        num_evens += 1

# Don't touch below this line

print(f"There are {num_evens} even numbers and {num_odds} odd numbers.")
