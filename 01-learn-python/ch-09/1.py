def remove_duplicates(spells):
    filtered_set = set()
    filtered_list = []
    for spell in spells:
        filtered_set.add(spell)
    for spell in filtered_set:
        filtered_list.append(spell)

    return filtered_list


# Don't edit below this line


def main():
    final = remove_duplicates(
        [
            "fireball",
            "eldrich blast",
            "fireball",
            "eldrich blast",
            "water gun",
            "eldrich blast",
            "water gun",
            "water gun",
            "fireball",
            "fireball",
            "sunburst",
            "fireball",
            "fireball",
        ]
    )
    final.sort()
    print(final)


main()
