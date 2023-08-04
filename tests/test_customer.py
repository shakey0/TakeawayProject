from lib.customer import *
from unittest.mock import Mock
import pytest

def test_customer_get_all_details():
    customer1 = Customer("01010101", "Lizzie", ["jk", "er"], "6 Blue Street", "+447111000111")
    assert customer1.get_all_details() == {"ID Number":"01010101", "Name":"Lizzie", "Allergens":["jk", "er"],
                                           "Address":"6 Blue Street", "Phone Number":"+447111000111"}

def test_customer_update_customer_details():
    customer1 = Customer("01010101", "Lizzie", ["jk", "er"], "6 Blue Street", "+447111000111")
    customer1.update_customer_details()
    assert customer1.get_all_details() == {"ID Number":"01010101", "Name":"Lizzie", "Allergens":["jk", "er"],
                                           "Address":"6 Blue Street", "Phone Number":"+447111000111"}
    customer1.update_customer_details(name="Elizabeth")
    assert customer1.get_all_details() == {"ID Number":"01010101", "Name":"Elizabeth", "Allergens":["jk", "er"],
                                           "Address":"6 Blue Street", "Phone Number":"+447111000111"}
    customer1.update_customer_details(phone_number="+447222111222")
    assert customer1.get_all_details() == {"ID Number":"01010101", "Name":"Elizabeth", "Allergens":["jk", "er"],
                                           "Address":"6 Blue Street", "Phone Number":"+447222111222"}
    customer2 = Customer("02020202", "Jonathan", ["ox"], "34 Red Street", "+447222000333")
    customer2.update_customer_details(address="59 Bird Street" ,phone_number="+447333111333")
    assert customer2.get_all_details() == {"ID Number":"02020202", "Name":"Jonathan", "Allergens":["ox"],
                                           "Address":"59 Bird Street", "Phone Number":"+447333111333"}
    customer3 = Customer("03030303", "Patrick", ["op", "wm", "gl"], "21 Orange Street", "+447333000333")
    customer3.update_customer_details(name="Paddy", address="11 Lion Street", phone_number="+447444111444")
    assert customer3.get_all_details() == {"ID Number":"03030303", "Name":"Paddy", "Allergens":["op", "wm", "gl"],
                                           "Address":"11 Lion Street", "Phone Number":"+447444111444"}
    
def test_customer_get_allergens():
    customer1 = Customer("01010101", "Lizzie", ["jk", "er"], "6 Blue Street", "+447111000111")
    assert customer1.get_allergens() == ["jk", "er"]

def test_customer_add_remove_allergens():
    customer1 = Customer("01010101", "Lizzie", ["jk", "er"], "6 Blue Street", "+447111000111")
    customer1.add_allergens(["to"])
    assert customer1.get_allergens() == ["jk", "er", "to"]
    assert customer1.get_all_details() == {"ID Number":"01010101", "Name":"Lizzie", "Allergens":["jk", "er", "to"],
                                           "Address":"6 Blue Street", "Phone Number":"+447111000111"}
    customer2 = Customer("02020202", "Jonathan", ["ox"], "34 Red Street", "+447222000333")
    customer2.add_allergens(["de", "qp", "mf"])
    assert customer2.get_allergens() == ["ox", "de", "qp", "mf"]
    assert customer2.get_all_details() == {"ID Number":"02020202", "Name":"Jonathan", "Allergens":["ox", "de", "qp", "mf"],
                                           "Address":"34 Red Street", "Phone Number":"+447222000333"}
    customer2.remove_allergens(["ox", "qp"])
    assert customer2.get_allergens() == ["de", "mf"]
    customer1.remove_allergens(["jk"])
    assert customer1.get_all_details() == {"ID Number":"01010101", "Name":"Lizzie", "Allergens":["er", "to"],
                                           "Address":"6 Blue Street", "Phone Number":"+447111000111"}
    customer2.remove_allergens(["de", "mf"])
    assert customer2.get_all_details() == {"ID Number":"02020202", "Name":"Jonathan", "Allergens":[],
                                           "Address":"34 Red Street", "Phone Number":"+447222000333"}
    
def test_customer_get_id():
    customer1 = Customer("01010101", "Lizzie", ["jk", "er"], "6 Blue Street", "+447111000111")
    assert customer1.get_id() == "01010101"

def test_customer_get_basket():
    customer1 = Customer("01010101", "Lizzie", ["jk", "er"], "6 Blue Street", "+447111000111")
    titles = ["Hornet Hummus", "Badger Burrito", "Tandoori Tiger", "Gerbil Gelato"]
    dish1, dish2, dish3, dish4 = Mock(), Mock(), Mock(), Mock()
    dish1.title, dish2.title, dish3.title, dish4.title = titles[0], titles[1], titles[2], titles[3]
    customer1.add_dish(dish3)
    assert customer1.get_basket() == [dish3]
    customer1.add_dish(dish1)
    customer1.add_dish(dish2)
    customer1.add_dish(dish2)
    customer1.add_dish(dish4)
    assert customer1.get_basket() == [dish3, dish1, dish2, dish2, dish4]
    customer1.remove_dish("Badger Burrito")
    customer1.add_dish(dish4)
    customer1.add_dish(dish4)
    assert customer1.get_basket() == [dish3, dish1, dish2, dish4, dish4, dish4]
    customer1.remove_dish("Tandoori Tiger")
    customer1.remove_dish("Badger Burrito")
    assert customer1.get_basket() == [dish1, dish4, dish4, dish4]
    with pytest.raises(Exception) as e:
        customer1.remove_dish("Dinosaur Dumplings")
    assert str(e.value) == "Dish not found in basket!"
    customer1.remove_dish("Hornet Hummus")
    customer1.remove_dish("Gerbil Gelato")
    customer1.remove_dish("Gerbil Gelato")
    customer1.remove_dish("Gerbil Gelato")
    assert customer1.get_basket() == []

def test_customer_confirm_order():
    customer1 = Customer("01010101", "Lizzie", ["jk", "er"], "6 Blue Street", "+447111000111")
    titles = ["Hornet Hummus", "Badger Burrito", "Tandoori Tiger", "Gerbil Gelato"]
    dish1, dish2, dish3, dish4 = Mock(), Mock(), Mock(), Mock()
    dish1.title, dish2.title, dish3.title, dish4.title = titles[0], titles[1], titles[2], titles[3]
    customer1.add_dish(dish3)
    customer1.add_dish(dish2)
    customer1.add_dish(dish2)
    customer1.add_dish(dish4)
    assert customer1.get_basket() == [dish3, dish2, dish2, dish4]
    assert customer1.confirm_order("010101010101") == [dish3, dish2, dish2, dish4]
    customer2 = Customer("02020202", "Jonathan", ["ox"], "34 Red Street", "+447222000333")
    customer2.add_dish(dish4)
    customer2.add_dish(dish1)
    customer2.remove_dish("Gerbil Gelato")
    customer2.add_dish(dish2)
    assert customer2.confirm_order("010101010101") == [dish1, dish2]

def test_customer_get_order_ids():
    customer1 = Customer("01010101", "Lizzie", ["jk", "er"], "6 Blue Street", "+447111000111")
    titles = ["Hornet Hummus", "Badger Burrito", "Tandoori Tiger", "Gerbil Gelato"]
    dish1, dish2, dish3, dish4 = Mock(), Mock(), Mock(), Mock()
    dish1.title, dish2.title, dish3.title, dish4.title = titles[0], titles[1], titles[2], titles[3]
    customer1.add_dish(dish3)
    customer1.add_dish(dish2)
    customer1.add_dish(dish2)
    customer1.add_dish(dish4)
    assert customer1.confirm_order("010101010101") == [dish3, dish2, dish2, dish4]
    assert customer1.get_order_ids() == ["010101010101"]
    customer1.add_dish(dish4)
    customer1.add_dish(dish1)
    customer1.remove_dish("Gerbil Gelato")
    customer1.add_dish(dish2)
    customer1.add_dish(dish3)
    assert customer1.confirm_order("010101010102") == [dish1, dish2, dish3]
    assert customer1.get_order_ids() == ["010101010101", "010101010102"]

def test_customer_get_phone_number():
    customer1 = Customer("01010101", "Lizzie", ["jk", "er"], "6 Blue Street", "+447111000111")
    assert customer1.get_phone_number() == "+447111000111"
    customer1.update_customer_details()
    assert customer1.get_phone_number() == "+447111000111"
    customer1.update_customer_details(phone_number="+447222111222")
    assert customer1.get_phone_number() == "+447222111222"
    customer1.update_customer_details(name="Liz", address="45 Stone Road", phone_number="+447222111222")
    assert customer1.get_phone_number() == "+447222111222"
    customer1.update_customer_details(name="Lizzy", address="45 Stone Road", phone_number="+447333222333")
    assert customer1.get_phone_number() == "+447333222333"
