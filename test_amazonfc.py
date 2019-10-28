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
        product.package(True, False, True, "Small")
        assert product.explosive == True
        assert product.fragile == False
        assert product.flammable == True
        assert product.box_size == "Small"
        assert product.packaged == True


def test_can_create_stamp_code():
    product = Product("Hair spray", "hair_spray.png", "Beauty & Personal Care", 234567)
    request = Request("somewhere", "short_distance", "Hair spray", 234567)
    product.req = request
    stamp_code = product.stamp_code("ABC-abc-1234")
    assert product.barcode == "ABC-abc-1234"
    assert product.address == "somewhere"

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

