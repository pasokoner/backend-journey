def calculate_damage(armor, weapon="fist"):
    if weapon == "fist":
        return armor - 5
    if weapon == "dagger":
        return armor - 10
    if weapon == "sword":
        return armor - 15

    return 0


# Don't touch below this line


def test(armor, weapon):
    dmg = 0
    if weapon is None:
        dmg = calculate_damage(armor)
        weapon = "fist"
    else:
        dmg = calculate_damage(armor, weapon)
    print(
        f"A soldier with {armor} armor was hit by a {weapon}! {dmg} damage was inflicted."
    )


test(5, "sword")
test(2, "dagger")
test(3, "dagger")
test(2, None)
test(2, "spell")
