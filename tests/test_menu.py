from lib.menu import *
from unittest.mock import Mock
import pytest

def test_menu_get_dish():
    titles = ["Hornet Hummus", "Badger Burrito", "Tandoori Tiger", "Gerbil Gelato"]
    dish1, dish2, dish3, dish4 = Mock(), Mock(), Mock(), Mock()
    dish1.title, dish2.title, dish3.title, dish4.title = titles[0], titles[1], titles[2], titles[3]
    menu = Menu()
    menu.add(dish1), menu.add(dish2)
    assert menu.get_dish("Badger Burrito") == dish2
    assert menu.get_dish("Hornet Hummus") == dish1
    with pytest.raises(Exception) as e:
        menu.get_dish("Gerbil Gelato")
    assert str(e.value) == "Dish not in list!"
    menu.add(dish3), menu.add(dish4)
    assert menu.get_dish("Tandoori Tiger") == dish3
    assert menu.get_dish("Gerbil Gelato") == dish4

def test_menu_get_most_popular_dishes():
    dish1, dish2, dish3, dish4, dish5 = Mock(), Mock(), Mock(), Mock(), Mock()
    dish6, dish7, dish8, dish9, dish10 = Mock(), Mock(), Mock(), Mock(), Mock()
    dish1.times_ordered, dish2.times_ordered, dish3.times_ordered, dish4.times_ordered = 0, 1, 2, 0
    dish5.times_ordered, dish6.times_ordered, dish7.times_ordered = 1, 0, 0
    dish8.times_ordered, dish9.times_ordered, dish10.times_ordered = 0, 0, 0
    menu = Menu()
    menu.add(dish1), menu.add(dish2), menu.add(dish3), menu.add(dish4), menu.add(dish5)
    menu.add(dish6), menu.add(dish7), menu.add(dish8), menu.add(dish9), menu.add(dish10)
    assert menu.get_most_popular_dishes() == [dish3, dish2, dish5]
    dish11, dish12, dish13, dish14, dish15 = Mock(), Mock(), Mock(), Mock(), Mock()
    dish16, dish17, dish18, dish19, dish20 = Mock(), Mock(), Mock(), Mock(), Mock()
    dish11.times_ordered, dish12.times_ordered, dish13.times_ordered, dish14.times_ordered = 38, 14, 22, 45
    dish15.times_ordered, dish16.times_ordered, dish17.times_ordered = 11, 1, 57
    dish18.times_ordered, dish19.times_ordered, dish20.times_ordered = 22, 15, 20
    menu.add(dish11), menu.add(dish12), menu.add(dish13), menu.add(dish14), menu.add(dish15)
    menu.add(dish16), menu.add(dish17), menu.add(dish18), menu.add(dish19), menu.add(dish20)
    assert menu.get_most_popular_dishes() == [dish17, dish14, dish11, dish13, dish18]
    dish21 = Mock()
    dish21.times_ordered = 22
    menu.add(dish21)
    assert menu.get_most_popular_dishes() == [dish17, dish14, dish11, dish13, dish18] or [dish17, dish14, dish11, dish13, dish21] or [dish17, dish14, dish11, dish18, dish21]

def test_menu_get_formatted_menu():
    list_of_dishes = []
    titles = ["Hornet Hummus", "Badger Burrito", "Tandoori Tiger", "Gerbil Gelato", "Flamingo Flapjacks",
              "Frog Fritters", "Giraffe Ginger Snaps", "Gnat Gnocchi", "Dragonfly Drumsticks", "Zebra Ziti"]
    calories = [460, 650, 590, 630, 560, 600, 580, 600, 570, 540]
    prices = [7.99, 8.99, 9.99, 7.49, 6.99, 7.49, 6.99, 8.49, 8.49, 8.99]
    for num in range(10):
        dictionary_menu = {}
        dictionary_menu["Title"] = titles[num]
        dictionary_menu["Calories"] = calories[num]
        dictionary_menu["Price"] = prices[num]
        list_of_dishes.append(dictionary_menu)
    dish1, dish2, dish3, dish4, dish5 = Mock(), Mock(), Mock(), Mock(), Mock()
    dish6, dish7, dish8, dish9, dish10 = Mock(), Mock(), Mock(), Mock(), Mock()
    dish1.times_ordered, dish2.times_ordered, dish3.times_ordered, dish4.times_ordered = 4, 1, 2, 5
    dish5.times_ordered, dish6.times_ordered, dish7.times_ordered = 1, 6, 5
    dish8.times_ordered, dish9.times_ordered, dish10.times_ordered = 0, 3, 4
    dish1.title, dish2.title, dish3.title, dish4.title = titles[0], titles[1], titles[2], titles[3]
    dish5.title, dish6.title, dish7.title = titles[4], titles[5], titles[6]
    dish8.title, dish9.title, dish10.title = titles[7], titles[8], titles[9]
    dish1.calories, dish2.calories, dish3.calories, dish4.calories = calories[0], calories[1], calories[2], calories[3]
    dish5.calories, dish6.calories, dish7.calories = calories[4], calories[5], calories[6]
    dish8.calories, dish9.calories, dish10.calories = calories[7], calories[8], calories[9]
    dish1.price, dish2.price, dish3.price, dish4.price = prices[0], prices[1], prices[2], prices[3]
    dish5.price, dish6.price, dish7.price = prices[4], prices[5], prices[6]
    dish8.price, dish9.price, dish10.price = prices[7], prices[8], prices[9]
    menu = Menu()
    menu.add(dish1), menu.add(dish2), menu.add(dish3), menu.add(dish4), menu.add(dish5)
    menu.add(dish6), menu.add(dish7), menu.add(dish8), menu.add(dish9), menu.add(dish10)
    assert menu.get_formatted_menu() == [("-" * 20) + "CUSTOMER FAVOURITES" + ("-" * 20),
                                         "Frog Fritters     600cal     £7.49",
                                         "Gerbil Gelato     630cal     £7.49",
                                         "Giraffe Ginger Snaps     580cal     £6.99",
                                         "Hornet Hummus     460cal     £7.99",
                                         "Zebra Ziti     540cal     £8.99",
                                         "",
                                         ("-" * 22) + "Selected Dishes" + ("-" * 22),
                                         "Badger Burrito     650cal     £8.99",
                                         "Tandoori Tiger     590cal     £9.99",
                                         "Flamingo Flapjacks     560cal     £6.99",
                                         "Gnat Gnocchi     600cal     £8.49",
                                         "Dragonfly Drumsticks     570cal     £8.49"]

from lib.dish import *

def test_menu_amend_dish_data():
    titles = ["Hornet Hummus", "Badger Burrito", "Tandoori Tiger", "Gerbil Gelato", "Flamingo Flapjacks",
              "Frog Fritters", "Giraffe Ginger Snaps", "Gnat Gnocchi", "Dragonfly Drumsticks", "Zebra Ziti"]
    calories = [460, 650, 590, 630, 560, 600, 580, 600, 570, 540]
    prices = [7.99, 8.99, 9.99, 7.49, 6.99, 7.49, 6.99, 8.49, 8.49, 8.99]
    dishes = [Dish(titles[num], calories[num], prices[num]) for num in range(10)]
    menu = Menu()
    for dish in dishes:
        menu.add(dish)
    menu.amend_dish_data(["mi", "sn", "rn"], [titles[1], titles[6], titles[6], titles[6], titles[8], titles[4]])
    assert dishes[0].get_times_ordered() == 0
    assert dishes[0].get_allergens() == {}
    assert dishes[1].get_times_ordered() == 1
    assert dishes[1].get_allergens() == {}
    assert dishes[4].get_times_ordered() == 1
    assert dishes[4].get_allergens() == {"mi":1}
    assert dishes[6].get_times_ordered() == 3
    assert dishes[6].get_allergens() == {"sn":3}
    menu.amend_dish_data(["rr", "af", "na"], [titles[1], titles[6], titles[7], titles[7]])
    assert dishes[1].get_times_ordered() == 2
    assert dishes[1].get_allergens() == {"rr":1}
    assert dishes[6].get_times_ordered() == 4
    assert dishes[6].get_allergens() == {"sn":3, "af":1, "na":1}
    assert dishes[7].get_times_ordered() == 2
    assert dishes[7].get_allergens() == {"na":2}