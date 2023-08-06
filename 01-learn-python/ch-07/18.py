def reverse_array(items):
    new_items = []
    for i in range(len(items) - 1, -1, -1):
        new_items.append(items[i])

    return new_items


# Don't touch below this line


def test(items):
    items_copy = items[:]
    reversed = reverse_array(items)
    print(f"{items_copy} reversed is: {reversed}")


test(["Shortsword", "Healing Potion", "Iron Breastplate", "Kite Shield"])
test(["Haste Potion", "Longsword", "Iron Bar", "Leather Scraps"])
test([1, 2, 300, 4, 5])
test(["now!", "order", "reverse", "in", "is", "Array", "This"])
test(["Kite Shield", "Iron Breastplate", "Healing Potion", "Shortsword"])
