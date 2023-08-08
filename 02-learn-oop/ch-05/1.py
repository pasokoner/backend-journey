class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


# don't touch below this line


def describe(rectangle):
    print(
        f"corner1: ({rectangle.x1},{rectangle.y1}) corner2: ({rectangle.x2},{rectangle.y2})"
    )


def main():
    describe(Rectangle(0, 0, 4, 4))
    describe(Rectangle(4, 4, 0, 0))
    describe(Rectangle(2, -2, 3, 4))


main()
