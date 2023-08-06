def merge(dict1, dict2):
    return {**dict1, **dict2}


def total_score(score_dict):
    total = 0
    for quarter in score_dict:
        total += score_dict[quarter]
    return total


# Don't touch below this line


def test(first_half, second_half):
    merged = merge(first_half, second_half)
    print(merged)
    total = total_score(merged)
    print(f"The team scored {total} points")


test(
    {"first_quarter": 24, "second_quarter": 31},
    {"third_quarter": 29, "fourth_quarter": 40},
)

test(
    {"first_quarter": 25, "second_quarter": 2},
    {"third_quarter": 31, "fourth_quarter": 0},
)


test(
    {"first_quarter": 12, "second_quarter": 2},
    {"third_quarter": 32, "fourth_quarter": 87},
)
