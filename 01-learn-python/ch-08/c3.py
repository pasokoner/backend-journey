def calculate_total(items_purchased, grocery_list):
    total = 0
    unpurchased_items = []

    for item in grocery_list:
        if item in items_purchased:
            total += grocery_list[item]
        else:
            unpurchased_items.append(item)

    return unpurchased_items, total


# Don't touch below this line


def test(items_purchased, grocery_list):
    unpurchased_items, total = calculate_total(items_purchased, grocery_list)
    print(f"You didn't purchase: {sorted(unpurchased_items)}")
    print(f"You paid: ${total:.2f}")


test(
    [
        "milk",
        "eggs",
        "bread",
        "cheese",
        "apples",
        "bananas",
        "lettuce",
        "cereal",
    ],
    {
        "milk": 2.50,
        "eggs": 3.25,
        "bread": 2.21,
        "cheese": 3.50,
        "apples": 4.44,
        "bananas": 2.88,
        "carrots": 3.89,
        "lettuce": 1.12,
        "potatoes": 6.21,
        "cereal": 4.99,
    },
)

test(
    [
        "milk",
        "bread",
        "cheese",
        "lettuce",
        "cereal",
    ],
    {
        "milk": 2.50,
        "eggs": 3.25,
        "bread": 1.21,
        "cheese": 3.50,
        "apples": 7.44,
        "bananas": 3.88,
        "carrots": 3.89,
        "lettuce": 1.12,
        "potatoes": 32.21,
        "cereal": 5.99,
    },
)

test(
    [
        "milk",
        "bread",
        "lettuce",
        "cereal",
    ],
    {
        "milk": 12.50,
        "eggs": 2.21,
        "bread": 1.23,
        "cheese": 3.50,
        "apples": 73.44,
        "bananas": 23.88,
        "carrots": 13.89,
        "lettuce": 12.12,
        "potatoes": 2.21,
        "cereal": 1.99,
    },
)
