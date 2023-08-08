class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return (self.width + self.length) * 2


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


# don't touch below this line


def test_rect(l, w):
    rect = Rectangle(l, w)
    print(f"Rectangle:")
    print(f" - Length: {l:.2f}")
    print(f" - Width: {w:.2f}")
    print(f" - Area: {rect.get_area():.2f}")
    print(f" - Perimeter: {rect.get_perimeter():.2f}")
    print("=====================================")


def test_square(l):
    square = Square(l)
    print(f"Square:")
    print(f" - Length: {l:.2f}")
    print(f" - Area: {square.get_area():.2f}")
    print(f" - Perimeter: {square.get_perimeter():.2f}")
    print("=====================================")


def main():
    test_rect(10.0, 5.0)
    test_rect(5.0, 10.0)
    test_square(2.0)
    test_square(7.0)


main()
