items = [
    "Potion",
    "Leather Scraps",
    "Bread",
    "Iron Ore",
    "Light Leather",
    "Bread",
    "Shortsword",
    "Longsword",
    "Iron Mace",
    "Shortsword",
    "Shortsword",
]

potion_count = 0
bread_count = 0
shortsword_count = 0

# don't touch above this line

for i in range(0, len(items)):
    if items[i] == "Potion":
        potion_count += 1
    if items[i] == "Bread":
        bread_count += 1
    if items[i] == "Shortsword":
        shortsword_count += 1

# don't touch below this line

print(f"You have {potion_count} potions in your inventory.")
print(f"You have {bread_count} pieces of bread in your inventory.")
print(f"You have {shortsword_count} shortswords in your inventory.")
