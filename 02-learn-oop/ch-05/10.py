class Sword:
    def __init__(self, type):
        self.type = type

    def __add__(self, other):
        if self.type == "bronze" and other.type == "bronze":
            return Sword("iron")
        if self.type == "iron" and other.type == "iron":
            return Sword("steel")

        raise Exception("can not craft")


# don't touch below this line


def main():
    try:
        sword1 = Sword("bronze")
        sword2 = Sword("bronze")
        print(f"creating sword1 that is {sword1.type} and sword2 that is {sword2.type}")
        print("crafting sword1 and sword2 into a new sword3...")
        sword3 = sword1 + sword2
        print(f"sword3 is {sword3.type}")
        sword4 = Sword("iron")
        print(f"creating sword4 that is {sword4.type}")
        print("crafting sword3 and sword4 into a new sword5...")
        sword5 = sword3 + sword4
        print(f"sword5 is {sword5.type}")

        sword6 = Sword("steel")
        print(f"creating sword6 that is {sword6.type}")
        print("crafting sword5 and sword6 into a new sword7...")
        sword7 = sword5 + sword6
        print(f"sword7 is {sword7.type}")
    except Exception as e:
        print(e)


main()
