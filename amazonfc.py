from typing import *

categories = ("automotive", "clothings", "electronics", "home and kitchen",
              "industrial", "sports", "tools", "toys and games")
shipping_box_size = ("12x12x12in", "16x16x16in", "18x18x18in", "22x22x22in",
                     "24x24x24in", "oversize")


class Shelf:
    def __init__(self, num):
        self.num = num
        self.content = [[Compartment() for i in range(4)] for i in range(4)]

    def get_comp(self, cords: str):
        row = ord(cords[0]) - 65
        column = int(cords[1]) - 1
        print(row, column)
        return self.content[row][column]


class Compartment:
    def __init__(self):
        self.content = []

    def __str__(self):
        return f"content: {self.content}"


class Product:
    def __init__(self, name: str, image: str, category: int):
        self.name = name
        self.image = image
        self.cat = categories[category]

    def __str__(self):
        return f"{self.name}, {self.cat}"

    def packaging(self, explosive: bool, fragile: bool, flammable: bool,
                  size: int):
        self.explosive = explosive
        self.fragile = fragile
        self.flamable = flamable
        self.box_size = shipping_box_size[size]
        self.packaged = True


def ship_in():
    pass


def ship_out(product: Product):
    pass


def get_product(requsted_product: str) -> Product:
    pass


storage = [Shelf(i+1) for i in range(8)]
