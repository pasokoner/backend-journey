def count_enemies(enemy_names):
    enemies = {}
    for name in enemy_names:
        if name in enemies:
            enemies[name] += 1
        else:
            enemies[name] = 1
    return enemies


# Don't edit below this line


def main():
    print(
        count_enemies(
            [
                "jackal",
                "kobold",
                "jackal",
                "kobold",
                "soldier",
                "kobold",
                "soldier",
                "soldier",
                "jackal",
                "jackal",
                "gremlin",
                "jackal",
                "jackal",
            ]
        )
    )


main()
