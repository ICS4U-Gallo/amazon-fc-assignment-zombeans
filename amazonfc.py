from typing import *

prod_categories = ("automotive", "clothings", "electronics",
                   "home and kitchen", "industrial", "sports",
                   "tools", "toys and games")
shipping_box_size = ("12x12x12in", "16x16x16in", "18x18x18in", "22x22x22in",
                     "24x24x24in", "oversize")
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
        self.dis = self.req.dis
        self.packaged = True

    def stamp_code(self, barcode):
        """Stamp barcode and address"""
        self.barcode = barcode
        self.address = self.req.address

    def check_danger():
        explosive = bool(input("Product explosive?(0 for no /1 for yes) "))
        fragile = bool(input("Product fragie?(0 for no /1 for yes) "))
        flammable = bool(input("Product flammable?(0 for no /1 for yes) "))
        return explosive, fragile, flammable

    def check_box_size():
        """Returns box size of the product"""
        size_num = int(input("Size Number"))
        size = shipping_box_size[size_num]
        return size


class Cart:
    all_carts = []

    def __init__(self):
        self.content = []
        Cart.all_carts.append(self)

    def add(self, item):
        self.content.append(item)

    def remove(self, item):
        self.content.remove(item)

    def scan_prod_to_shelf(product, shelf_num, comp_code):
        """Put Product in shelf/compartment"""
        comp = storage[shelf_num-1].get_comp(comp_code)
        comp.add(product)


class Bin(Cart):
    def __init__(self):
        super().__init__()

    def package(req: Request):
        for prod in self.content:
            prod.package(prod.check_danger(), prod.check_box_size())
        self.packaged = True

    def send_to_truck(self, truck):
        """Send product to truck"""
        for product in self.content:
            self.remove(product)
            truck.add(product)


class Truck:
    def __init__(self, types):
        self.type = distance[types]
        self.content = []

    def loading(self, prod):
        self.content.append(prod)

    def leave(self):
        del self


class Request:
    prod_request = []

    def __init__(self, address, distance, prod_name, prod_code):
        self.loc = address
        self.dis = distance
        self.prod_name = prod_name
        self.prod_code = prod_code
        Request.prod_request.append(self)

    def get_prod_id():
        id_list = []
        for req in prod_request:
            id_list.append(req.prod_code)
        return id_list

    def link_prod(bins):
        for req in Request.prod_request:
            for prod in bins:
                if prod.code == req.prod_code:
                    prod.req = req
                    break


#Ship In
def scan_prod_to_trolly(trolly):
    """Create Product and put in trolly"""
    name = input("Prod Name: ")
    image = input("Image: ")
    category = prod_categories[int(input("Category Number: "))]
    code = int(input("Prod Code: "))
    product = Product(name, image, category, code)
    trolly.append(product)


#Ship Out
def display_box_type():
    """Display shipping box type on screen"""
    box_type = int(input("Enter type of box"))
    print(box_type)


def order_fulfillment(storage, bins):
    for shelf in storage:
        get_prod_from_shelf(shelf, Request.get_prod_id(), bins)
    Request.link_prod(bins)
    bins.package()


def display_prod(product):
    """Display product"""
    print(product)


def get_prod_request():
    loc = input("Location: ")
    dis = distance[int(input("Distance Type: "))]
    prod_name = input("Prod Name: ")
    prod_code = input("Prod Code: ")
    request = Request(loc, dis, prod_name, prod_code)


def get_prod_from_shelf(shelf, prod_req_id, bins):
    """Scan product to bin from shelf"""
    for i in range(len(shelf.content)):
        for j in range(len(shelf.content[i])):
            for prod in shelf.content[i][j]:
                if prod.code in prod_req_id:
                    bins.add(prod)
                    shelf.content[i][j].remove(prod)


storage = [Shelf(i+1) for i in range(8)]
trolly = Cart()
bins = Cart()
