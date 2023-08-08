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

    def use_arrows(self, num):
        if self.get_num_arrows() - num <= 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= num


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        self.use_arrows(3)
        print(f"{target.get_name()} was shot by 3 crossbow bolts")


# don't touch below this line


def main():
    try:
        print("creating an archer named Bard")
        human2 = Archer("Bard", 1)
        identify(human2)
        print(f"Bard has {human2.get_num_arrows()} arrows")

        print("creating a crossbowman named Sir Not-Appearing-In-This-Film")
        human3 = Crossbowman("Sir Not-Appearing-In-This-Film", 4)
        identify(human3)
        print(f"{human3.get_name()} has {human3.get_num_arrows()} arrows")
        print(f"{human3.get_name()} attempts to shoot {human2.get_name()}")
        human3.triple_shot(human2)
        print(f"{human3.get_name()} has {human3.get_num_arrows()} arrows")
        print(f"{human3.get_name()} attempts to shoot {human2.get_name()}")
        human3.triple_shot(human2)

    except Exception as e:
        print(e)


def identify(human):
    print(f"Getting name: {human.get_name()}")


main()
