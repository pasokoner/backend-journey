def remove_duplicates(lst):
    return {item for item in lst}


# Don't touch below this line


def test(lst):
    removed = sorted(remove_duplicates(lst))
    print(f"Variable 'removed' is of type: {type(removed)}")
    print("List after duplicates removed:")
    for item in removed:
        print(f"- {item}")
    print("---")


test(["basketball", "football", "soccer", "baseball", "basketball"])
test(
    [
        "Age of Empires",
        "World of Warcraft",
        "Halo",
        "Call of Duty",
        "Age of Empires",
        "Magic the Gathering",
        "Halo",
    ]
)
test(
    [
        "Lane",
        "Allan",
        "James",
        "Tiffany",
        "John",
        "Cameron",
        "Lane",
        "Allan",
        "James",
        "Tiffany",
        "John",
        "Cameron",
        "Chad",
        "Tj",
        "Tim",
        "Gertrude",
        "Stephanie",
    ]
)
