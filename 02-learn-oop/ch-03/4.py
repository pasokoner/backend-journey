class Human:
    def sprint_right(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()

        self.__pos_x += self.__speed * 2

    def sprint_left(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()

        self.__pos_x -= self.__speed * 2

    def sprint_up(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()

        self.__pos_y += self.__speed * 2

    def sprint_down(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()

        self.__pos_y -= self.__speed * 2

    def __raise_if_cannot_sprint(self):
        if self.__stamina <= 0:
            raise Exception("not enough mana to sprint")

    def __use_sprint_stamina(self):
        self.__stamina -= 1

    # don't touch below this line

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y

    def __init__(self, pos_x, pos_y, speed, stamina):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina


def main():
    try:
        print("creating a human. x=0 y=0 speed=5")
        human = Human(0, 0, 5, 3)
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("sprinting left...")
        human.sprint_left()
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("sprinting left...")
        human.sprint_left()
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("moving right...")
        human.move_right()
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("moving up...")
        human.move_up()
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("sprinting up...")
        human.sprint_up()
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("sprinting down...")
        human.sprint_down()
        print_position(human)
    except Exception as e:
        print(e)


def print_position(human):
    x, y = human.get_position()
    print(f"Your human is at x={x}, y={y}")


main()
