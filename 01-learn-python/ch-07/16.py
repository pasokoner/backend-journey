def should_serve_customer(customer_age, on_break, time):
    return (time >= 5 and time <= 10) and not on_break and customer_age >= 21


# don't touch below this line


def test(customer_age, on_break, time):
    should_serve = should_serve_customer(customer_age, on_break, time)
    print(
        f"age={customer_age}, on_break={on_break}, time={time}: should_serve={should_serve}"
    )


test(22, False, 8)
test(41, False, 1)
test(22, True, 8)
test(18, True, 3)
test(23, False, 9)
test(22, False, 11)
test(21, False, 9)
test(20, False, 9)
