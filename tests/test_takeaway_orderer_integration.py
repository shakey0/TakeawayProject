from lib.takeaway_orderer import *
import pytest

def test_takeaway_orderer_init():
    takeaway_orderer = TakeawayOrderer("menu.csv", ['Mouse', 'Whale', 'Anteater', 'Pig', 'Albatross',
                                                    'Vulture', 'Human', 'Mongoose', 'Scorpion', 'Badger',
                                                    'Oyster', 'Okapi', 'Termite', 'Nightingale', 'Eagle'])
    assert len(takeaway_orderer.menu.all_dishes) == 15
    assert takeaway_orderer.menu.all_dishes[1].title == "Whale Wonton"
    assert takeaway_orderer.menu.all_dishes[8].price == 7.49
    assert takeaway_orderer.menu.all_dishes[11].calories == 420

def test_takeaway_orderer_show_menu():
    takeaway_orderer = TakeawayOrderer("menu.csv", ['Stingray', 'Whale', 'Anteater', 'Pig', 'Albatross',
                                                    'Vulture', 'Squirrel', 'Mongoose', 'Scorpion', 'Badger',
                                                    'Oyster', 'Okapi', 'Termite', 'Swan', 'Shark'])
    takeaway_orderer.menu.all_dishes[7].ordered()
    takeaway_orderer.menu.all_dishes[7].ordered()
    takeaway_orderer.menu.all_dishes[9].ordered()
    takeaway_orderer.menu.all_dishes[9].ordered()
    takeaway_orderer.menu.all_dishes[12].ordered()
    takeaway_orderer.menu.all_dishes[12].ordered()
    takeaway_orderer.menu.all_dishes[7].ordered()
    takeaway_orderer.menu.all_dishes[12].ordered()
    takeaway_orderer.menu.all_dishes[5].ordered()
    takeaway_orderer.menu.all_dishes[4].ordered()
    takeaway_orderer.menu.all_dishes[4].ordered()
    assert takeaway_orderer.show_menu() == [[1, "CUSTOMER FAVOURITES", 1],
                                            ["Mongoose Madras", "630cal", "£8.99"],
                                            ["Tandoori Termite", "590cal", "£9.99"],
                                            ["Albatross Alfredo", "700cal", "£11.99"],
                                            ["Badger Burrito", "650cal", "£8.99"],
                                            ["Vulture Vindaloo", "590cal", "£9.99"],
                                            [1, 1, 1],
                                            [1, "Selected Dishes", 1],
                                            ["Stingray Stroganoff", "680cal", "£10.99"],
                                            ["Whale Wonton", "600cal", "£8.49"],
                                            ["Anteater Alfredo", "700cal", "£11.99"],
                                            ["Pig Paella", "520cal", "£7.49"],
                                            ["Squirrel Scones", "600cal", "£7.49"],
                                            ["Scorpion Scones", "600cal", "£7.49"],
                                            ["Oyster Omelette", "420cal", "£7.49"],
                                            ["Okapi Omelette", "420cal", "£7.49"],
                                            ["Swiss Swan", "540cal", "£11.99"],
                                            ["Shark Schnitzel", "570cal", "£8.99"]]

def test_takeaway_orderer_add_customer():
    takeaway_orderer = TakeawayOrderer("menu.csv", ['Stingray', 'Whale', 'Anteater', 'Pig', 'Albatross',
                                                    'Vulture', 'Squirrel', 'Mongoose', 'Scorpion', 'Badger',
                                                    'Oyster', 'Okapi', 'Termite', 'Swan', 'Shark'])
    assert len(takeaway_orderer.add_customer("Lizzie", ["jk", "er"], "6 Blue Street", "+447111000111")) == 8
    assert type(takeaway_orderer.add_customer("Jonathan", ["ox"], "34 Red Street", "+447222000333")) == str
    assert takeaway_orderer.add_customer("Patrick", ["op", "wm", "gl"], "21 Orange Street", "+447333000333").isnumeric()
    assert len(takeaway_orderer.order_data.get_all_customers()) == 3
    assert takeaway_orderer.order_data.get_all_customers()[0].address == "6 Blue Street"
    assert takeaway_orderer.order_data.get_all_customers()[2].allergens == ["op", "wm", "gl"]
    assert takeaway_orderer.order_data.get_all_customers()[1].phone_number == "+447222000333"
    assert takeaway_orderer.order_data.get_all_customers()[1].name == "Jonathan"

def test_takeaway_orderer_show_menu_with_allergens():
    takeaway_orderer = TakeawayOrderer("menu.csv", ['Stingray', 'Whale', 'Anteater', 'Pig', 'Albatross',
                                                    'Vulture', 'Squirrel', 'Mongoose', 'Scorpion', 'Badger',
                                                    'Oyster', 'Okapi', 'Termite', 'Swan', 'Shark'])
    takeaway_orderer.menu.all_dishes[7].ordered()
    takeaway_orderer.menu.all_dishes[7].ordered()
    takeaway_orderer.menu.all_dishes[9].ordered()
    takeaway_orderer.menu.all_dishes[9].ordered()
    takeaway_orderer.menu.all_dishes[12].ordered()
    takeaway_orderer.menu.all_dishes[12].ordered()
    takeaway_orderer.menu.all_dishes[7].ordered()
    takeaway_orderer.menu.all_dishes[12].ordered()
    takeaway_orderer.menu.all_dishes[5].ordered()
    takeaway_orderer.menu.all_dishes[4].ordered()
    takeaway_orderer.menu.all_dishes[4].ordered()
    customer1_id = takeaway_orderer.add_customer("Lizzie", ["jk", "re"], "6 Blue Street", "+447111000111")
    customer2_id = takeaway_orderer.add_customer("Jonathan", ["ox"], "34 Red Street", "+447222000333")
    customer3_id = takeaway_orderer.add_customer("Patrick", ["st", "wm", "dg", "og"], "21 Orange Street", "+447333000333")
    menu1 = [[1, "CUSTOMER FAVOURITES", 1],
            ["Mongoose Madras", "630cal", "£8.99"],
            ["Tandoori Termite", "590cal", "£9.99"],
            ["Albatross Alfredo (Contains re!)", "700cal", "£11.99"],
            ["Badger Burrito", "650cal", "£8.99"],
            ["Vulture Vindaloo (Contains re!)", "590cal", "£9.99"],
            [1, 1, 1],
            [1, "Selected Dishes", 1],
            ["Stingray Stroganoff", "680cal", "£10.99"],
            ["Whale Wonton", "600cal", "£8.49"],
            ["Anteater Alfredo (Contains re!)", "700cal", "£11.99"],
            ["Pig Paella", "520cal", "£7.49"],
            ["Squirrel Scones (Contains re!)", "600cal", "£7.49"],
            ["Scorpion Scones", "600cal", "£7.49"],
            ["Oyster Omelette", "420cal", "£7.49"],
            ["Okapi Omelette", "420cal", "£7.49"],
            ["Swiss Swan", "540cal", "£11.99"],
            ["Shark Schnitzel", "570cal", "£8.99"]]
    assert takeaway_orderer.show_menu_with_allergens(customer1_id) == menu1
    menu2 = [[1, "CUSTOMER FAVOURITES", 1],
            ["Mongoose Madras", "630cal", "£8.99"],
            ["Tandoori Termite", "590cal", "£9.99"],
            ["Albatross Alfredo", "700cal", "£11.99"],
            ["Badger Burrito", "650cal", "£8.99"],
            ["Vulture Vindaloo", "590cal", "£9.99"],
            [1, 1, 1],
            [1, "Selected Dishes", 1],
            ["Stingray Stroganoff", "680cal", "£10.99"],
            ["Whale Wonton", "600cal", "£8.49"],
            ["Anteater Alfredo", "700cal", "£11.99"],
            ["Pig Paella", "520cal", "£7.49"],
            ["Squirrel Scones", "600cal", "£7.49"],
            ["Scorpion Scones", "600cal", "£7.49"],
            ["Oyster Omelette", "420cal", "£7.49"],
            ["Okapi Omelette", "420cal", "£7.49"],
            ["Swiss Swan", "540cal", "£11.99"],
            ["Shark Schnitzel", "570cal", "£8.99"]]
    assert takeaway_orderer.show_menu_with_allergens(customer2_id) == menu2
    menu3 = [[1, "CUSTOMER FAVOURITES", 1],
            ["Mongoose Madras", "630cal", "£8.99"],
            ["Tandoori Termite", "590cal", "£9.99"],
            ["Albatross Alfredo", "700cal", "£11.99"],
            ["Badger Burrito (Contains dg!)", "650cal", "£8.99"],
            ["Vulture Vindaloo", "590cal", "£9.99"],
            [1, 1, 1],
            [1, "Selected Dishes", 1],
            ["Stingray Stroganoff (Contains st and og!)", "680cal", "£10.99"],
            ["Whale Wonton", "600cal", "£8.49"],
            ["Anteater Alfredo", "700cal", "£11.99"],
            ["Pig Paella", "520cal", "£7.49"],
            ["Squirrel Scones", "600cal", "£7.49"],
            ["Scorpion Scones", "600cal", "£7.49"],
            ["Oyster Omelette (Contains st!)", "420cal", "£7.49"],
            ["Okapi Omelette", "420cal", "£7.49"],
            ["Swiss Swan", "540cal", "£11.99"],
            ["Shark Schnitzel", "570cal", "£8.99"]]
    assert takeaway_orderer.show_menu_with_allergens(customer3_id) == menu3

def test_takeaway_orderer_show_customer_details_and_update_customer_details():
    takeaway_orderer = TakeawayOrderer("menu.csv", ['Stingray', 'Whale', 'Anteater', 'Pig', 'Albatross',
                                                    'Vulture', 'Squirrel', 'Mongoose', 'Scorpion', 'Badger',
                                                    'Oyster', 'Okapi', 'Termite', 'Swan', 'Shark'])
    customer1_id = takeaway_orderer.add_customer("Lizzie", ["jk", "er"], "6 Blue Street", "+447111000111")
    customer1_details = {"ID Number":customer1_id, "Name":"Lizzie", "Allergens":["jk", "er"],
                        "Address":"6 Blue Street", "Phone Number":"+447111000111"}
    assert takeaway_orderer.show_customer_details(customer1_id) == customer1_details

    takeaway_orderer.update_customer_details(customer1_id)
    assert takeaway_orderer.show_customer_details(customer1_id) == customer1_details

    customer1_details2 = {"ID Number":customer1_id, "Name":"Lizzie", "Allergens":["jk", "er"],
                        "Address":"47 Swan Drive", "Phone Number":"+447111000111"}
    takeaway_orderer.update_customer_details(customer1_id, address="47 Swan Drive")
    assert takeaway_orderer.show_customer_details(customer1_id) == customer1_details2

    customer1_details3 = {"ID Number":customer1_id, "Name":"Elizabeth", "Allergens":["jk", "er"],
                        "Address":"47 Swan Drive", "Phone Number":"+447222111222"}
    takeaway_orderer.update_customer_details(customer1_id, name="Elizabeth", phone_number="+447222111222")
    assert takeaway_orderer.show_customer_details(customer1_id) == customer1_details3

def test_takeaway_orderer_get_add_remove_customer_allergens():
    takeaway_orderer = TakeawayOrderer("menu.csv", ['Stingray', 'Whale', 'Anteater', 'Pig', 'Albatross',
                                                    'Vulture', 'Squirrel', 'Mongoose', 'Scorpion', 'Badger',
                                                    'Oyster', 'Okapi', 'Termite', 'Swan', 'Shark'])
    customer1_id = takeaway_orderer.add_customer("Lizzie", ["jk", "er"], "6 Blue Street", "+447111000111")
    assert takeaway_orderer.get_customer_allergens(customer1_id) == ["jk", "er"]
    takeaway_orderer.add_customer_allergens(customer1_id, ["fb"])
    assert takeaway_orderer.get_customer_allergens(customer1_id) == ["jk", "er", "fb"]
    takeaway_orderer.remove_customer_allergens(customer1_id, ["er"])
    assert takeaway_orderer.get_customer_allergens(customer1_id) == ["jk", "fb"]
    takeaway_orderer.add_customer_allergens(customer1_id, ["fb", "oe", "wq"])
    assert takeaway_orderer.get_customer_allergens(customer1_id) == ["jk", "fb", "oe", "wq"]
    takeaway_orderer.remove_customer_allergens(customer1_id, ["fb", "wq"])
    assert takeaway_orderer.get_customer_allergens(customer1_id) == ["jk", "oe"]
    takeaway_orderer.add_customer_allergens(customer1_id, ["jk", "oe", "rr"])
    assert takeaway_orderer.get_customer_allergens(customer1_id) == ["jk", "oe", "rr"]
    with pytest.raises(Exception) as e:
        takeaway_orderer.remove_customer_allergens(customer1_id, ["fb", "wq"])
    assert str(e.value) == "Allergen not found!"

def test_takeaway_orderer_add_remove_dish_to_from_basket_view_basket():
    takeaway_orderer = TakeawayOrderer("menu.csv", ['Stingray', 'Whale', 'Anteater', 'Pig', 'Albatross',
                                                    'Vulture', 'Squirrel', 'Mongoose', 'Scorpion', 'Badger',
                                                    'Oyster', 'Okapi', 'Termite', 'Swan', 'Shark'])
    customer1_id = takeaway_orderer.add_customer("Lizzie", ["jk", "er"], "6 Blue Street", "+447111000111")

    assert takeaway_orderer.add_dish_to_basket(customer1_id, "Pig Paella") == "Pig Paella was added to your basket."
    assert takeaway_orderer.view_basket(customer1_id) == [["Pig Paella", "520cal", "£7.49"]]
    
    assert takeaway_orderer.add_dish_to_basket(customer1_id, "Badger Burrito (Contains er!)") == "Badger Burrito (Contains er!) was added to your basket."
    assert takeaway_orderer.view_basket(customer1_id) == [["Pig Paella", "520cal", "£7.49"],
                                                            ["Badger Burrito (Contains er!)", "650cal", "£8.99"]]
    
    assert takeaway_orderer.remove_dish_from_basket(customer1_id, "Pig Paella") == "Pig Paella was removed from your basket."
    assert takeaway_orderer.view_basket(customer1_id) == [["Badger Burrito (Contains er!)", "650cal", "£8.99"]]

    takeaway_orderer.add_customer_allergens(customer1_id, ["rr"])
    assert takeaway_orderer.add_dish_to_basket(customer1_id, "Badger Burrito (Contains er and rr!)") == "Badger Burrito (Contains er and rr!) was added to your basket."
    assert takeaway_orderer.add_dish_to_basket(customer1_id, "Squirrel Scones (Contains rr!)") == "Squirrel Scones (Contains rr!) was added to your basket."
    assert takeaway_orderer.view_basket(customer1_id) == [["Badger Burrito (Contains er and rr!)", "650cal", "£8.99"],
                                                        ["Badger Burrito (Contains er and rr!)", "650cal", "£8.99"],
                                                        ["Squirrel Scones (Contains rr!)", "600cal", "£7.49"]]
    with pytest.raises(Exception) as e:
        takeaway_orderer.remove_dish_from_basket(customer1_id, "Pig Paella")
    assert str(e.value) == "Pig Paella was not in basket!"
    assert takeaway_orderer.remove_dish_from_basket(customer1_id, "Badger Burrito (Contains er and rr!)") == "Badger Burrito was removed from your basket."
    assert takeaway_orderer.remove_dish_from_basket(customer1_id, "Squirrel Scones (Contains rr!)") == "Squirrel Scones was removed from your basket."
    assert takeaway_orderer.view_basket(customer1_id) == [["Badger Burrito (Contains er and rr!)", "650cal", "£8.99"]]

def test_takeaway_orderer_confirm_order_and_view_past_orders():
    takeaway_orderer = TakeawayOrderer("menu.csv", ['Stingray', 'Whale', 'Anteater', 'Pig', 'Albatross',
                                                    'Vulture', 'Squirrel', 'Mongoose', 'Scorpion', 'Badger',
                                                    'Oyster', 'Okapi', 'Termite', 'Swan', 'Shark'])
    customer1_id = takeaway_orderer.add_customer("Lizzie", ["jk", "er"], "6 Blue Street", "+447111000111")
    assert takeaway_orderer.view_past_orders(customer1_id) == []
    assert takeaway_orderer.add_dish_to_basket(customer1_id, "Pig Paella") == "Pig Paella was added to your basket."
    assert takeaway_orderer.add_dish_to_basket(customer1_id, "Badger Burrito (Contains er!)") == "Badger Burrito (Contains er!) was added to your basket."
    assert takeaway_orderer.view_past_orders(customer1_id) == []
    order1_id, date, time = takeaway_orderer.confirm_order(customer1_id)
    assert takeaway_orderer.menu.all_dishes[3].get_times_ordered() == 1
    assert takeaway_orderer.menu.all_dishes[3].get_allergens() == {}
    assert takeaway_orderer.menu.all_dishes[9].get_times_ordered() == 1
    assert takeaway_orderer.menu.all_dishes[9].get_allergens() == {"er":1}
    assert takeaway_orderer.view_past_orders(customer1_id) == [{"Order No.":order1_id,
                                                                "Dishes":["Pig Paella", "Badger Burrito"],
                                                                "Date":date, "Time":time}]

    takeaway_orderer.add_customer_allergens(customer1_id, ["rr"])
    assert takeaway_orderer.add_dish_to_basket(customer1_id, "Badger Burrito (Contains er and rr!)") == "Badger Burrito (Contains er and rr!) was added to your basket."
    assert takeaway_orderer.add_dish_to_basket(customer1_id, "Squirrel Scones (Contains rr!)") == "Squirrel Scones (Contains rr!) was added to your basket."
    order2_id, date2, time2 = takeaway_orderer.confirm_order(customer1_id)
    assert takeaway_orderer.menu.all_dishes[3].get_times_ordered() == 1
    assert takeaway_orderer.menu.all_dishes[9].get_times_ordered() == 2
    assert takeaway_orderer.menu.all_dishes[9].get_allergens() == {"er":2, "rr":1}
    assert takeaway_orderer.menu.all_dishes[6].get_times_ordered() == 1
    assert takeaway_orderer.menu.all_dishes[6].get_allergens() == {"rr":1}
    assert takeaway_orderer.view_past_orders(customer1_id) == [{"Order No.":order1_id,
                                                                "Dishes":["Pig Paella", "Badger Burrito"],
                                                                "Date":date, "Time":time},
                                                                {"Order No.":order2_id,
                                                                "Dishes":["Badger Burrito", "Squirrel Scones"],
                                                                "Date":date2, "Time":time2}]
