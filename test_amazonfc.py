from amazonfc import *

def test_can_create_product():
    product = Product("Baby powder", "babypowder.png", "Health & Personal Care", 123456)
    assert product.name == "Baby powder"
    assert product.image == "babypowder.png"
    assert product.cate == "Health & Personal Care"
    assert product.code == 123456

    product = Product("chromebook", "chromebook.png", "Electronics", 123457)
    assert product.name == "chromebook"
    assert product.image == "chromebook.png"
    assert product.cate == "Electronics"
    assert product.code == 123457

    product = Product("Lotion", "lotion.png", "Health & Personal Care", 123556)
    assert product.name == "Lotion"
    assert product.image == "lotion.png"
    assert product.cate == "Health & Personal Care"
    assert product.code == 123556

    
def test_can_create_package():
    product = Product("Hair spray", "hair_spray.png", "Beauty & Personal Care", 234567)
    product.package(True, False, True, "Small")
    assert product.explosive == True
    assert product.fragile == False
    assert product.flammable == True
    assert product.box_size == "Small"
    assert product.packaged == True

    request = Request("somewhere", "short_distance", "Hair spray", 234567)
    product.req = request
    stamp_code = product.stamp_code("ABC-abc-1234")
    assert product.barcode == "ABC-abc-1234"
    assert product.address == "somewhere"

    
def test_can_use_cart():
    product = Product("Hair spray", "hair_spray.png", "Beauty & Personal Care", 234567)
    cart = Cart()
    cart.add(product)
    assert cart.content[0] == product
    cart.remove(product)
    assert len(cart.content) == 0


def test_can_create_bin():
    bin_1 = Bin()
    assert bin_1.content == []
    assert bin_1.id == 0
  
    product = Product("Hair spray", "hair_spray.png", "Beauty & Personal Care", 234567)
    bin_1.add(product)
    assert bin_1.content[0] == product

    bin_1.remove(product)
    assert bin_1.content == []

    
def test_compartment():
    compartment = Compartment()
    assert compartment.content == []
    prod = Product("Hair spray", "hair_spray.png", "Beauty & Personal Care", 234567)

    compartment.add(prod)
    assert compartment.content[0] == prod

    compartment.remove(prod)
    assert compartment.content == []


def test_truck():
    truck = Truck(1)
    assert truck.content == []
    assert truck.type == "mid_range"
    assert truck.id == 0

    product = Request("1234 sesame street", "mid_range", "table", 444)
    truck.loading(product)
    assert truck.content[0] == product

    truck.leave()
    assert truck.content == []


def test_request():
    request = Request("123 pitbull street", "International", "chromebook", 123)
    assert request.address == "123 pitbull street"
    assert request.dis == "International"
    assert request.prod_name == "chromebook"
    assert request.prod_code == 123

    request = Request("1234 sesame street", "Local", "table", 444)
    assert request.address == "1234 sesame street"
    assert request.dis == "Local"
    assert request.prod_name == "table"
    assert request.prod_code == 444

    request = Request("12345 king street", "International", "Book", 555)
    assert request.address == "12345 king street"
    assert request.dis == "International"
    assert request.prod_name == "Book"
    assert request.prod_code == 555
