from amazonfc import *

def test_can_create_shelf():
    pass

def test_can_create_product():
    product = Product("Baby powder", "babypowder.png", "Health & Personal Care", 123456)
    assert product.name == "Baby powder"
    assert product.image == "babypowder.png"
    assert product.cat == "Health & Personal Care"
    assert product.code == 123456


def test_can_create_package():
        product = Product("Hair spray", "hair_spray.png", "Beauty & Personal Care", 234567)
        package = product.package(True, False, True, "Small")
        assert package.explosive == True
        assert package.fragile == False
        assert package.flammable == True
        assert package.box_size == "Small"
        assert package.packaged == True


def test_can_create_stamp_code():
    product = Product("Hair spray", "hair_spray.png", "Beauty & Personal Care", 234567)
    stamp_code = product.stamp_code(ABC-abc-1234)
    assert stamp_code.barcode == ABC-abc-1234

def test_check_danger():
    product = Product("Hair spray", "hair_spray.png", "Beauty & Personal Care", 234567)
    check_danger == product.check_danger()
    check_danger.explosive = 1
    check_danger.fragile = 0
    check_danger.flammable = 1


def test_check_box_size():
    product = Product("Hair spray", "hair_spray.png", "Beauty & Personal Care", 234567)
    check_box_size = product.check_box_size()
    

def test_can_create_cart():
    pass


def test_add():
    pass


def test_remove():
    pass


def test_scan_prod_to_shelf():
    pass


def test_can_create_bin():
    pass


def test_package():
    pass


def test_send_to_truck():
    pass


def test_can_create_truck():
    pass


def test_loading():
    pass


def test_leave():
    pass


def test_can_create_request():
    pass


def test_get_prod_id():
    pass


def test_link_prod():
    pass


def test_scan_prod_to_trolly():
    pass


def test_display_box_type():
    pass


def test_order_fulfillment():
    pass


def test_display_prod():
    pass


def test_get_prod_request():
    pass


def test_get_prod_from_shelf():
    pass
