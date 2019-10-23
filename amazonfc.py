from typing import *

prod_categories = ("automotive", "clothings", "electronics", "home and kitchen", "industrial", "sports", "tools", "toys and games")
shipping_box_size = ("12x12x12in", "16x16x16in", "18x18x18in", "22x22x22in", "24x24x24in", "oversize")
distance = ("short_distance", "mid_range", "long_distance", "international")

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

    def add(self, prod):
        self.content.append(prod)

    def remove(self, prod):
        self.content.remove(prod)    


class Product:
    def __init__(self, name: str, image: str, category: int, code: int):
        self.name = name
        self.image = image
        self.cat = prod_categories[category]
        self.code = code
    
    def __str__(self):
        return f"{self.name}, {self.cat}, {self.code}"

    def packaging(self, explosive: bool, fragile: bool, flamable: bool, size: int):
        self.explosive = explosive
        self.fragile = fragile
        self.flamable = flamable
        self.box_size = shipping_box_size[size]
        self.packaged = True


class Cart:
    def __init__(self):
        self.content = []

    def add(self, item):
        self.content.append(item)

    def remove(self, item):
        self.content.remove(item)


class Truck:
    def __init__(self, types):
        self.type = distance[types]
        self.content = []

    def loading(self, prod):
        self.content.append(prod)

    def leave(self):
        del self
    

#Ship In
def scan_prod_to_trolly():
    """Create Product and move to trolly"""
    pass


def scan_prod_to_shelf():
    """Put Product from trolly to shelf/compartment"""
    pass


#Ship Out
def display_box_type():
    """Display shipping box type on screen"""
    pass


def stamp_code():
    """Stamp barcode and address"""
    pass


def send_to_truck():
    """Product send to truck"""
    pass


#Order Fulfillment
def display_prod():
    """Display product"""
    pass


def get_prod_from_shelf():
    """Scan product out of shelf"""
    pass


def put_prod_in_bin():
    """Place product into bin"""
    pass


def package_bin():
    """Send bin to packaging"""
    pass


storage = [Shelf(i+1) for i in range(8)]
trolly = Cart()
bins = Cart()