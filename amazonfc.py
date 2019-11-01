from typing import *
import pickle

prod_categories = ("automotive", "clothings", "electronics",
                   "home and kitchen", "industrial", "sports",
                   "tools", "toys and games")
shipping_box_size = ("12x12x12in", "16x16x16in", "18x18x18in", "22x22x22in",
                     "24x24x24in", "obese")
distance = ("short_distance", "mid_range", "long_distance", "international")


class Shelf:
    """Shelf class
    Attributes:
        num(int): Shelf number
        content(List): 2-d array of compartments
    """
    def __init__(self, num: int):
        """ Creates a shelf
        Args:
            num(int): The shelf number
        """
        self.num = num
        self.content = [[Compartment() for i in range(4)] for i in range(4)]

    def get_comp(self, code: str):
        """Get compartment from the coordinate
        Args:
            code(str): Coordinate of compartment

        Returns:
            compartment(Compartment)
        """
        row = ord(code[0]) - 65
        column = int(code[1]) - 1
        return self.content[row][column]


class Compartment:
    """Compartment class
    Attributes:
        prod(object): Product found in compartment
    """
    def __init__(self):
        self.content = []

    def __str__(self):
        return f"content: {self.content}"

    def add(self, prod: object):
        self.content.append(prod)

    def remove(self, prod: object):
        self.content.remove(prod)


class Product:
    """Product class
    Attributes:
        name(str): Name of product
        image(str): Picture of product
        category(str): Category product falls into
        code(int): Code of product

    """
    def __init__(self, name: str, image: str, category: str, code: int):
        self.name = name
        self.image = image
        self.cate = category
        self.code = code

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.cate, self.code)

    def package(self, explosive: bool, fragile: bool, flammable: bool,
                size: str):
        self.explosive = explosive
        self.fragile = fragile
        self.flammable = flammable
        self.box_size = size
        self.packaged = True

    def stamp_code(self, barcode):
        """Stamp barcode and address"""
        if self.packaged:
            self.barcode = barcode
            self.address = self.req.address
            self.dis = self.req.dis
            self.stamped = True

    def check_danger():
        """Asks user if product is dangerous"""
        explosive = bool(input("Is the product explosive?(0 for no /1 for yes) \n"))
        fragile = bool(input("Is the product fragie?(0 for no /1 for yes) \n"))
        flammable = bool(input("Is the product flammable?(0 for no /1 for yes) \n"))
        return explosive, fragile, flammable

    def check_box_size():
        """Returns box size of the product"""
        size_num = int(input("Size Number: "))
        size = shipping_box_size[size_num]
        return size


class Cart:
    """Class to move product to shelf
    Attributes:
        item(object): The product
        shelf_num(int): Shelf number product is stored in
        comp_coor(str): Coordinate of product in shelf
    """

    all_carts = []
    id = 0

    def __init__(self):
        self.content = []
        self.id = Cart.id
        Cart.all_carts.append(self)
        Cart.id += 1

    def __str__(self):
        return "id: {}, # of item: {}".format(self.id, len(self.content))

    def add(self, item: object):
        """Add item to list"""
        self.content.append(item)

    def remove(self, item: object):
        """Remove item from list"""
        self.content.remove(item)

    def scan_prod_to_shelf(self, shelf_num: int, comp_coor: str):
        """Put Product in shelf/compartment"""
        for prod in self.content:
            comp = storage[shelf_num-1].get_comp(comp_coor)
            comp.add(product)
            self.content.remove(prod)


class Bin():
    """Class for where products are packaged"""

    all_bins = []
    id = 0

    def __init__(self):
        self.content = []
        self.id = Bin.id
        Bin.all_bins.append(self)
        Bin.id += 1

    def __str__(self):
        return "id: {}, # of item: {}".format(self.id, len(self.content))

    def add(self, item: object):
        """Add item to list"""
        self.content.append(item)

    def remove(self, item: object):
        """Remove item from list"""
        self.content.remove(item)

    def package(self):
        for prod in self.content:
            prod.package(prod.check_danger(), prod.check_box_size())
        self.packaged = True

    def send_to_truck(self):
        """Send product to truck"""
        for prod in self.content:
            if prod.stamped:
                for truck in Truck.all_trucks:
                    if prod.dis == truck.type:
                        truck.add(prod)
                        self.remove(prod)
                        break


class Truck:
    """Class for dlivery truck
    Attributes:
        types(int): Gives you the type of truck
        prod(object): Product that will be placed in truck
    """

    all_trucks = []
    id = 0

    def __init__(self, types: int):
        self.type = distance[types]
        self.content = []
        self.id = Truck.id
        Truck.all_trucks.append(self)
        Truck.id += 1

    def __str__(self):
        return "id: {}, type: {}, # of item: {}"\
            .format(self.id, self.type, len(self.content))

    def loading(self, prod):
        if prod.dis == self.type:
            self.content.append(prod)

    def leave(self):
        self.content = []


class Request:
    """Class for when people request products
    Attributes:
        address(str): Address of person buying
        distance(str): Type of truck needed
        prod_name(str): Name of product
        prod_code(int): Product code
    """
    prod_request = []

    def __init__(self, address: str, distance: str, prod_name: str,
                 prod_code: int):
        self.address = address
        self.dis = distance
        self.prod_name = prod_name
        self.prod_code = prod_code
        Request.prod_request.append(self)

    def __str__(self):
        return "address: {}, distance: {}, product name: {}, product code: {}"\
            .format(self.addr, self.dis, self.prod_name, self.prod_code)

    @staticmethod
    def get_prod_id():
        id_list = []
        for req in Request.prod_request:
            id_list.append(req.prod_code)
        return id_list

    @staticmethod
    def link_prod(bins):
        for req in Request.prod_request:
            for prod in bins.content:
                if prod.code == req.prod_code:
                    prod.req = req
                    break


def scan_prod_to_trolly(trolly):
    """Create Product and put in trolly"""
    name = input("Product Name: ")
    image = input("Image: ")
    category = prod_categories[int(input("Category Number: "))]
    code = int(input("Product Code: "))
    product = Product(name, image, category, code)
    trolly.add(product)


def display_box_type(prod):
    """Display shipping box type on screen"""
    print(prod.box_size)


def display_prod(product):
    """Display product"""
    print(product)


def get_prod_request():
    loc = input("Location: ")
    dis = distance[int(input("Distance Type(0, 1, 2, 3): \n"))]
    prod_name = input("Product Name: ")
    prod_code = input("Product Code: ")
    request = Request(loc, dis, prod_name, prod_code)


def get_prod_from_shelf(shelf, prod_req_id, bins):
    """Scan product to bin from shelf"""
    for i in range(len(shelf.content)):
        for j in range(len(shelf.content[i])):
            for prod in shelf.content[i][j].content:
                if prod.code in prod_req_id:
                    bins.add(prod)
                    shelf.content[i][j].remove(prod)


def save():
    global storage
    with open("amazonfcsave", "wb") as output:
        pickle.dump(storage, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(Cart.all_carts, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(Truck.all_trucks, output, pickle.HIGHEST_PROTOCOL)


def load():
    global storage
    with open("amazonfcsave", "rb") as input_:
        storage = pickle.load(input_)
        Cart.all_carts = pickle.load(input_)
        Truck.all_trucks = pickle.load(input_)


def ship_in(trolly):
    while True:
        input_ = input("Input 'a' to create product and place in trolly."
                       "\nInput 'b' to place product in shelf.\n").upper()
        if input_ == "":
            break
        elif input_ == "A":
            scan_prod_to_trolly(trolly)
        elif input_ == "B":
            shelf_num = int(input("Input shelf num: "))
            comp_cord = input("Input compartment coordinates: ")
            trolly.scan_prod_to_shelf(shelf_num, comp_cord)


def order_fulfillment(storage, bins):
    while True:
        input_ = input("Input 'a' to create product and its destination."
                       "\nInput 'b' to move product from shelf into bins."
                       "\nInput 'c' to package product.\n").upper()
        if input_ == "":
            break
        elif input_ == "A":
            addr = input("Input address: ")
            dis = distance[int(input("Input distance type code"
                                     "(0, 1, 2, or 3): "))]
            prod_name = input("Input products name: ")
            prod_code = int(input("Input products code(must be a number): "))
            Request(addr, dis, prod_name, prod_code)
        elif input_ == "B":
            for shelf in storage:
                get_prod_from_shelf(shelf, Request.get_prod_id(), bins)
            Request.link_prod(bins)
        elif input_ == "C":
            bins.package()


def ship_out(bins):
    while True:
        input_ = input("Input 'a' to enter code of product."
                       "\nInput 'b' to send bin to truck."
                       "\n Input 'c' to send truck to destination.\n").upper()
        if input_ == "":
            break
        elif input_ == "A":
            for prod in bins:
                code = input("Enter code of product: ")  
                prod.stamp_code(code)
        elif input_ == "B":
            bins.send_to_truck()
        elif input_ == "C":
            for truck in Truck.all_trucks:
                print("Truck has left.")
                truck.leave()


def display(storage):
    while True:
        input_ = input("Input 'a' to show which items are in which shelf."
                       "\nInput 'b' to show all requested products."
                       "\nInput 'c' to show products in cart."
                       "\nInput 'd' to print items in truck.\n").upper()
        if input_ == "":
            break
        elif input_ == "A":
            shelf_num = int(input("Input shelf number: "))
            comp_cord = input("Input compartment coordinates: ").upper()
            comp = storage[shelf_num-1].get_comp(comp_cord)
            print("shelf:{} compartment:{}, content: ".format(shelf_num,
                                                              comp_cord))
            for prod in comp.content:
                print(prod)
        elif input_ == "B":
            print("All products requested: ")
            for req in Request.prod_request:
                print(req)
        elif input_ == "C":
            for cart in Cart.all_carts:
                print(cart)
                for prod in cart.content:
                    print(prod)
                print()
        elif input_ == "D":
            for truck in Truck.all_trucks:
                print(truck)
                for prod in truck.content:
                    print(prod)
                print()


def main():
    global storage
    storage = [Shelf(i+1) for i in range(8)]
    trolly = Cart()
    bins = Bin()
    truck1 = Truck(0)
    truck2 = Truck(1)
    truck3 = Truck(2)
    truck4 = Truck(3)
    while True:
        input_ = input("Input 'A' to place your order. \nInput 'B' to "
                       "place item in shelf. \nInput 'c' to send product out."
                       "\nInput 'd' to display storage. \nInput 's' to"
                       "save. \nInput 'l' to load.\n").upper()
        if input_ == "A":
            order_fulfillment(storage, bins)
        elif input_ == "B":
            ship_in(trolly)
        elif input_ == "C":
            ship_out(bins)
        elif input_ == "D":
            display(storage)
        elif input_ == "S":
            save()
        elif input_ == "L":
            load()


if __name__ == "__main__":
    main()
