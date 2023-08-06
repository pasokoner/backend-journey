def string_exists(string_to_check, string_array):
    for name in string_array:
        if string_to_check == name:
            return True
    return False


# Don't touch below this line


def test(string_to_check, string_array):
    exists = string_exists(string_to_check, string_array)
    if exists:
        print(f"{string_to_check} exists in {string_array}")
    else:
        print(f"{string_to_check} does NOT exist in {string_array}")


test("Healing Potion", ["Iron Bar", "Leather Scraps", "Shortsword"])
test("Iron Helmet", ["Buckler", "Leather Armor Kit", "Iron Breastplate"])
test("Iron Ore", ["Healing Potion", "Iron Ore", "Cheese"])
test("Shortsword", ["Potion", "Iron Breastplate", "Shortsword"])
