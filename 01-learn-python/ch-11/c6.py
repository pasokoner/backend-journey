for n in range(1, 100):
    fizzbuzz = ""
    if n % 3 == 0:
        fizzbuzz += "fizz"
    if n % 5 == 0:
        fizzbuzz += "buzz"

    if len(fizzbuzz):
        print(fizzbuzz)
    else:
        print(n)
