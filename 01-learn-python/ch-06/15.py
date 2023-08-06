odd_numbers = []

# don't touch above this line

for i in range(0, 300):
    if i & 1:
        odd_numbers.append(i)

# don't touch below this line

print(odd_numbers)
