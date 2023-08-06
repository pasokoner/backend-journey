player_power = 101
enemy_defense = 100
advantage, disadvantage, evenly_matched = False, False, False

# Do not touch above this line

advantage = player_power > enemy_defense
disadvantage = player_power < enemy_defense
evenly_matched = player_power == enemy_defense

# Do not touch below this line

if advantage:
    print("You have the advantage!")
elif disadvantage:
    print("You have the disadvantage!")
else:
    print("You are evenly matched!")
