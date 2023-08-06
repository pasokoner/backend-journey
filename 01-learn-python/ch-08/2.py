def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}",
    }


# Don't edit below this line


def main():
    rec = get_character_record("bloodwarrior123", "server1", 5, 1)
    print_rec(rec)

    rec = get_character_record("fronzenboi", "server2", 2, 1)
    print_rec(rec)

    rec = get_character_record("slasher69", "server3", 2, 5)
    print_rec(rec)


def print_rec(rec):
    print(f"name: {rec['name']}")
    print(f"server: {rec['server']}")
    print(f"level: {rec['level']}")
    print(f"rank: {rec['rank']}")
    print(f"id: {rec['id']}")
    print("---")


main()
