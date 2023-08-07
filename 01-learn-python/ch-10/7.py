def handle_get_player_record(player_id):
    try:
        return get_player_record(player_id)
    except IndexError:
        print("index is too high")
    except Exception:
        print(Exception)


# Don't edit below this line


def get_player_record(player_id):
    if player_id < 0:
        # custom exception
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    # possible IndexError
    return players[player_id]


def test(player_id):
    player_record = handle_get_player_record(player_id)
    if player_record is not None:
        print(player_record)


def main():
    test(0)
    test(1)
    test(2)
    test(3)
    test(-1)


main()
