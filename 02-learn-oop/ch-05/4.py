class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.fire_range = fire_range
        self.height = height
        self.width = width
        self.__hitbox = Rectangle(
            pos_x - (width / 2),
            pos_y - (height / 2),
            pos_x + (width / 2),
            pos_y + (height / 2),
        )

    def in_area(self, x_1, y_1, x_2, y_2):
        target = Rectangle(x_1, y_1, x_2, y_2)

        return target.overlaps(self.__hitbox)

    # don't touch below this line

    def breathe_fire(self, x, y, units):
        print(f"{self.name} breathes fire at {x}/{y} with range {self.fire_range}")
        for unit in units:
            in_area = unit.in_area(
                x - self.fire_range,
                y - self.fire_range,
                x + self.fire_range,
                y + self.fire_range,
            )
            if in_area:
                print(f"{unit.name} is hit by the fire")


class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_left_x(self):
        if self.x1 < self.x2:
            return self.x1
        return self.x2

    def get_right_x(self):
        if self.x1 > self.x2:
            return self.x1
        return self.x2

    def get_top_y(self):
        if self.y1 > self.y2:
            return self.y1
        return self.y2

    def get_bottom_y(self):
        if self.y1 < self.y2:
            return self.y1
        return self.y2


def describe(dragon):
    print(
        f"{dragon.name} is at position ({dragon.pos_x},{dragon.pos_y}). height: {dragon.height}. width: {dragon.width}. fire range: {dragon.fire_range}"
    )


def main():
    dragons = [
        Dragon("Green Dragon", -1, -2, 1, 2, 1),
        Dragon("Red Dragon", 2, 2, 2, 2, 2),
        Dragon("Blue Dragon", 4, -3, 2, 1, 1),
        Dragon("Black Dragon", 5, -1, 3, 2, 2),
    ]

    for i in range(0, len(dragons)):
        dragon = dragons[i]
        describe(dragon)

    for i in range(0, len(dragons)):
        dragon = dragons[i]
        other_dragons = dragons.copy()
        del other_dragons[i]
        dragon.breathe_fire(i, i, other_dragons)


main()
