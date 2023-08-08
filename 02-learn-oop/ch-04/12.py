class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        if (self.pos_x >= x_1 and self.pos_x <= x_2) and (
            self.pos_y >= y_1 and self.pos_y <= y_2
        ):
            return True

        return False


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        for unit in units:
            if unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            ):
                print(f"{unit.name} is hit by the fire")


# don't touch below this line


def main():
    print("Creating an army of generic units")
    units = [
        Unit("Yvor", 1, 0),
        Unit("Nicholas", 0, 1),
        Unit("Eoin", 2, 0),
        Unit("Cian", 3, 3),
        Unit("Andrew", -1, 4),
        Unit("Baran", -6, 5),
        Unit("Carbry", 2, 1),
    ]
    for unit in units:
        print(f"creating {unit.name} at position {unit.pos_x} {unit.pos_y}")

    smaug = Dragon("Smaug", 6, 6, 2)
    print(f"{smaug.name} breathes fire at position 1,1")
    smaug.breathe_fire(1, 1, units)


main()
