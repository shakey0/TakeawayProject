from lib.order_data import *
from unittest.mock import Mock
import pytest

def test_order_data_get_customer():
    customer1, customer2, customer3 = Mock(), Mock(), Mock()
    customer1.customer_id, customer2.customer_id, customer3.customer_id = "12121212", "13131313", "14141414"
    order_data = OrderData()
    order_data.add_customer(customer1), order_data.add_customer(customer2), order_data.add_customer(customer3)
    assert order_data.get_customer("12121212") == customer1
    with pytest.raises(Exception) as e:
        order_data.get_customer("1313131")
    assert str(e.value) == "Customer ID does not match required length!"
    with pytest.raises(Exception) as e:
        order_data.get_customer("15151515")
    assert str(e.value) == "Customer doesn't exist!"
    customer4 = Mock()
    customer4.customer_id = "15151515"
    order_data.add_customer(customer4)
    assert order_data.get_customer("15151515") == customer4

def test_order_data_get_order():
    order1, order2, order3 = Mock(), Mock(), Mock()
    order1.order_id, order2.order_id, order3.order_id = "121212121212", "131313131313", "141414141414"
    order_data = OrderData()
    order_data.add_order(order1), order_data.add_order(order2), order_data.add_order(order3)
    assert order_data.get_order("141414141414") ==  order3
    with pytest.raises(Exception) as e:
        order_data.get_order("13131313131")
    assert str(e.value) == "Order ID does not match required length!"
    with pytest.raises(Exception) as e:
        order_data.get_order("151515151515")
    assert str(e.value) == "Order doesn't exist!"
    order4 = Mock()
    order4.order_id = "151515151515"
    order_data.add_order(order4)
    assert order_data.get_order("151515151515") == order4
