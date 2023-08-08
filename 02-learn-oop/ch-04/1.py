class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows


# don't touch below this line


def main():
    try:
        print("creating a human named Faramir")
        human = Human("Faramir")
        identify(human)
    except Exception as e:
        print(e)

    try:
        print("creating an archer named Bard")
        human = Archer("Bard", 1)
        identify(human)
        print(f"Bard has {human.get_num_arrows()} arrows")
    except Exception as e:
        print(e)


def identify(human):
    print(f"Getting name: {human.get_name()}")


main()
