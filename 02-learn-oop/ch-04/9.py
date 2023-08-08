class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target):
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10)


# Create the Wizard class here
class Wizard(Hero):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.__mana = mana

    def cast(self, target):
        if self.__mana < 25:
            raise Exception("not enough mana")

        self.__mana -= 25
        target.take_damage(25)


# don't touch below this line


def main():
    health = 100
    mana = 400
    print(f"Creating a Wizard named Harry with {health} health and {mana} mana")
    human1 = Wizard("Harry", health, mana)
    identify(human1)

    health = 100
    arrows = 2
    print(f"Creating an Archer named Pericles with {health} health and {arrows} arrows")
    human2 = Archer("Pericles", health, arrows)
    identify(human2)

    while human1.get_health() > 0 and human2.get_health() > 0:
        try:
            print(f"{human2.get_name()} attempts to shoot {human1.get_name()}")
            human2.shoot(human1)
            identify(human1)
            identify(human2)
        except Exception as e:
            print(e)

        try:
            print(f"{human1.get_name()} attempts to cast at {human2.get_name()}")

            human1.cast(human2)
            identify(human1)
            identify(human2)
        except Exception as e:
            print(e)


def identify(human):
    print(f"Name: {human.get_name()}, health: {human.get_health()}")


main()
