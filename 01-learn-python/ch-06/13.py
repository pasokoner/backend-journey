inventory = ["Potion", "Healing Potion", "Iron Breastplate", "Leather Scraps"]

# don't touch above this line

found = False
for item in inventory:
    if item == "Leather Scraps":
        found = True

# don't touch below this line

if found:
    print("Found the leather scraps!")
else:
    print("Couldn't find the leather scraps!")
