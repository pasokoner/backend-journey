def area_sum(rectangles):
    total = 0

    for rect in rectangles:
        total += rect["height"] * rect["width"]

    return total


# don't touch below this line


def test(rects):
    sum = area_sum(rects)
    print(f"sum is {sum}")


test([{"height": 4, "width": 5}])
test([{"height": 4, "width": 5}, {"height": 4, "width": 9}, {"height": 18, "width": 5}])
test(
    [
        {"height": 4, "width": 5},
        {"height": 8, "width": 5},
        {"height": 19, "width": 5},
        {"height": 21, "width": 5},
    ]
)
