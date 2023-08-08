class Rectangle:
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


# don't touch below this line


def describe(rectangle):
    print(
        f"left x: {rectangle.get_left_x()}, right x: {rectangle.get_right_x()}, top y: {rectangle.get_top_y()}, bottom y: {rectangle.get_bottom_y()}"
    )


def main():
    describe(Rectangle(0, 0, 4, 4))
    describe(Rectangle(4, 4, 0, 0))
    describe(Rectangle(1, 2, 3, 4))
    describe(Rectangle(3, 4, 1, 2))


main()
