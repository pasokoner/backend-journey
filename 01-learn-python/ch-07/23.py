# TODO no. 1
def filter_messages(messages):
    counter = 0
    filtered = []

    for message in messages:
        temp_message = []

        for word in message.split():
            if word == "dang":
                counter += 1
            else:
                temp_message.append(word)

        filtered.append(" ".join(temp_message))
    print(filtered, counter)

    return filtered, counter


# Don't edit below this line


def main():
    messages = [
        "well dang it",
        "dang the whole dang thing",
        "kill that knight, dang it",
        "get him!",
        "donkey kong",
        "oh come on, get them",
        "run away from the dang baddies",
    ]
    filtered_messages, words_removed = filter_messages(messages)
    if len(filtered_messages) != len(words_removed):
        print("filtered_messages and words_removed lists should be the same size")
        return
    for i in range(0, len(filtered_messages)):
        print(
            f"Removed {words_removed[i]} words. Censored text: '{filtered_messages[i]}'"
        )


main()
