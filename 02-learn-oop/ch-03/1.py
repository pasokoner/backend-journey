class Human:
    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return (self.__pos_x, self.__pos_y)

    # don't touch below this line

    def __init__(self, pos_x, pos_y, speed):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed


def main():
    print("creating a human. x=0 y=0 speed=5")
    human = Human(0, 0, 5)
    print_position(human)

    print("moving left...")
    human.move_left()
    print_position(human)

    print("moving left...")
    human.move_left()
    print_position(human)

    print("moving right...")
    human.move_right()
    print_position(human)

    print("moving up...")
    human.move_up()
    print_position(human)

    print("moving up...")
    human.move_up()
    print_position(human)

    print("moving down...")
    human.move_down()
    print_position(human)


def print_position(human):
    x, y = human.get_position()
    print(f"Your human is at x={x}, y={y}")


main()
