def get_first_item(items):
    if len(items):
        return items[0]

    return "ERROR"


# Don't touch below this line


def test(items):
    first = get_first_item(items)
    print(f"First item in {items} is: {first}")


test([1, 2])
test(["Healing Potion"])
test(["Iron Ore", "Iron Bar", "Scimitar"])
test([])
