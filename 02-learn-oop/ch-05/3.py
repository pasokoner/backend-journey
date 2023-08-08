class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    # don't touch below this line

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


def describe(r):
    print(
        f"left x: {r.get_left_x()}, bottom y: {r.get_bottom_y()}, right x: {r.get_right_x()}, top y: {r.get_top_y()}"
    )


def test(r1, r2):
    print("describing r1")
    describe(r1)
    print("describing r2")
    describe(r2)
    print(f"r1 overlaps r2: {r1.overlaps(r2)}")
    print(f"r2 overlaps r1: {r2.overlaps(r1)}")
    print("========")


def main():
    r1 = Rectangle(0, 0, 4, 4)
    r2 = Rectangle(3, 3, 6, 6)
    test(r1, r2)

    r1 = Rectangle(0, 0, 4, 4)
    r2 = Rectangle(5, 5, 8, 8)
    test(r1, r2)

    r1 = Rectangle(0, 0, 4, 4)
    r2 = Rectangle(4, 4, 8, 8)
    test(r1, r2)


main()
