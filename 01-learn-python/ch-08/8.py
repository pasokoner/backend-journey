def get_most_common_enemy(enemies_dict):
    name = None
    max_so_far = float("-inf")

    for enemy in enemies_dict:
        if enemies_dict[enemy] > max_so_far:
            name = enemy
            max_so_far = enemies_dict[enemy]

    return name


# Don't edit below this line


def test(enemies_dict):
    most_common = get_most_common_enemy(enemies_dict)
    print(f"Using dict: {enemies_dict}")
    print(f"Most common: {most_common}")
    print("----")


def main():
    test({"jackal": 4, "kobold": 3, "soldier": 10, "gremlin": 5})
    test({"jackal": 1, "kobold": 3, "soldier": 2, "gremlin": 5})
    test({"jackal": 2, "gremlin": 7})


main()
