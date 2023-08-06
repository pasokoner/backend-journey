heroes = [
    (
        "Glorfindel",
        2093,
        True,
    ),
    (
        "Gandalf",
        1054,
        False,
    ),
    (
        "Gimli",
        389,
        False,
    ),
    (
        "Aragorn",
        87,
        False,
    ),
]

# Don't touch below this line

for hero in heroes:
    print(f"name: {hero[0]}, age: {hero[1]}, is_elf: {hero[2]}")
