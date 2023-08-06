number_of_employees = 102

c_level_bonus = 2000
manager_bonus = 1000
standard_bonus = 500

# C Level Executives
sarah_id = 1
mary_id = 2

# Managers
john_id = 6
bob_id = 44
joe_id = 18

dollars_needed = 0

# Don't touch above this line

for i in range(number_of_employees):
    if sarah_id == i or mary_id == i:
        dollars_needed += c_level_bonus
    elif john_id == i or bob_id == i or joe_id:
        dollars_needed += manager_bonus
    else:
        dollars_needed += standard_bonus

# Don't touch below this line

print(f"{dollars_needed} dollars are needed to fulfill all bonuses")
