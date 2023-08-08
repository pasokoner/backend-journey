class Dragon:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"I am {self.name}, the {self.color} dragon"


# don't touch below this line


def main():
    print(Dragon("Smaug", "red"))
    print(Dragon("Saphira", "blue"))
    print(Dragon("Nefarian", "black"))
    print(Dragon("Toothless", "blackish"))


main()
