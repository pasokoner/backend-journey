def does_attack_hit(attack_roll, armor_class):
    return attack_roll != 1 and attack_roll >= armor_class


def test(attack_roll, armor_class):
    hits = does_attack_hit(attack_roll, armor_class)
    if hits:
        print(
            f"With a roll of {attack_roll} and armor class of {armor_class} the attack hits!"
        )
    else:
        print(
            f"With a roll of {attack_roll} and armor class of {armor_class} the attack does NOT hit!"
        )


test(17, 18)
test(20, 25)
test(1, 0)
test(16, 13)
test(25, 21)
