def count_nested_levels(nested_comments, target_comment_id, level=1):
    # if target_comment_id in nested_comments:
    #     return level

    if target_comment_id in nested_comments:
        return level

    max_nested_level = -1

    for key in nested_comments.keys():
        # return count_nested_levels(nested_comments[key], target_comment_id, level)
        level_found = count_nested_levels(
            nested_comments[key], target_comment_id, level + 1
        )
        print(max_nested_level, level_found)

        max_nested_level = max(max_nested_level, level_found)

    return max_nested_level


# {
#     1: {
#         3: {

#         },
#         4: {

#         }
#     }
# }


# don't touch below this line


def test(nested_comments, target_comment_id):
    result = count_nested_levels(nested_comments, target_comment_id)
    print(f"Nested levels of comment {target_comment_id}: {result}")
    print("====================================")


def main():
    test_comments = {
        1: {
            2: {
                3: {},
                4: {5: {}},
            },
            6: {},
            7: {8: {9: {10: {}}}},
        }
    }
    test(test_comments, 1)
    test(test_comments, 2)
    test(test_comments, 3)
    test(test_comments, 5)
    test(test_comments, 10)


main()
