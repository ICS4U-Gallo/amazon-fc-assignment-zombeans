from typing import *

storage = [[0 for i in range(11)] for i in range(9)]
categories = ("automotive", "clothings", "electronics", "home and kitchen", "industrial", "sports", "tools", "toys and games")
shipping_box_size = ("12x12x12in", "16x16x16in", "18x18x18in", "22x22x22in", "24x24x24in", "oversize")

class Product:
    def __init__(self, name: str, image: str, category: int, compartment_num: int):
        self.name = name
        self.image = image
        self.cat = categories[category]
        self.shelf_num = category
    
    def put_item_in_compartment(self, compartment_num: int):
        if storage[self.shelf_num][compartment_num] == 0:
            self.compartment_num = compartment_num
            storage[shelf_num][compartment_num] = self


    def packaging(self, explosive: bool, fragile: bool, flamable: bool, size: int):
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

