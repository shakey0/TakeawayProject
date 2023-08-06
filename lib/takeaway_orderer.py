from lib.customer import *
from lib.menu import *
from lib.dish import *
from lib.customer import *
from lib.order_data import *
from lib.order import *
import os
from datetime import datetime
import random
from list_of_animals import *

class TakeawayOrderer:

    # creates self.menu (an instance of the Menu class)
    # creates self.order_data (an instance of the OrderData class)
    def __init__(self, menu_csv, animal_list):
        self.menu = Menu()
        menu_data = self.get_file_contents(menu_csv)[1:]
        chosen_animals = []
        for n in range(15):
            while True:
                animal = animal_list[n]
                if animal not in chosen_animals:
                    break
            chosen_animals.append(animal)
            dish_item = self.match_dish_to_animal(menu_data, animal)
            dish_info = dish_item.split(";")
            title, calories, price = self.create_dish_title(animal, dish_info[0]), dish_info[1], dish_info[2]
            self.menu.add(Dish(title, int(calories), float(price)))
        self.order_data = OrderData()
    
    # supplementary method for the get_file_contents method
    def does_file_exist(self, filename):
        return os.path.isfile(filename)
    
    # supplementary method for the __init__ method
    def get_file_contents(self, filename):
        if self.does_file_exist(filename):
            with open(filename, "r") as file:
                text = file.readlines()
            return [line[:-3] for line in text]
        else:
            return "This file cannot be found!"

    # supplementary method for the __init__ method
    def match_dish_to_animal(self, menu_data, animal):
        first_letters = 2
        while first_letters > 0:
            for item in menu_data:
                if animal[0:first_letters].lower() == item[0:first_letters].lower():
                    return item
            first_letters -= 1
        raise Exception("Match not found!")

    # supplementary method for the __init__ method
    def create_dish_title(self, animal, dish_title):
        if all(word.isalpha() for word in dish_title.split()):
            return f"{animal.title()} {dish_title}"
        else:
            if any(char=="1" for char in dish_title):
                return f"{dish_title[:-1]} {animal.title()}"
            else:
                return f"{animal.title()} {dish_title[3:]}"

    # EXTERNAL method - returns the menu as a list of lists
    def show_menu(self):
        return self.menu.get_listed_menu()
    
    # supplementary method for the add_customer and confirm_order methods
    def make_id(self, length):
        while True:
            exists = False
            generated_number = str(random.randint(1, length))
            while len(generated_number) < len(str(length)):
                generated_number = "0" + generated_number
            for customer in self.order_data.get_all_customers():
                if customer.customer_id == generated_number:
                    exists = True
            if not exists:
                return generated_number
    
    # EXTERNAL method - gives the customer information to self.order_data (an instance of the OrderData
    # class) which then creates and stores it in an instance of the Customer class
    def add_customer(self, name, allergens, address, phone_number):
        unique_customer_id = self.make_id(99999999)
        self.order_data.add_customer(Customer(unique_customer_id, name, allergens, address, phone_number))
        return unique_customer_id

    # supplementary method for the show_menu_with_allergens and view_basket methods
    def add_allergens_to_food_titles(self, listed_items, allergens):
        menu_with_allergens = []
        for line in listed_items:
            if isinstance(line[0], int):
                menu_with_allergens.append(line)
                continue
            found_allergens = []
            for allergen in allergens:
                if allergen in line[0].lower():
                    found_allergens.append(allergen)
            if len(found_allergens) > 0:
                amended_line = [f"{line[0]} (Contains {' and '.join(found_allergens)}!)", line[1], line[2]]
                menu_with_allergens.append(amended_line)
            else:
                menu_with_allergens.append(line)
        return menu_with_allergens

    # EXTERNAL method - shows the menu with the customers allergens
    def show_menu_with_allergens(self, customer_id):
        allergens = self.order_data.get_customer(customer_id).get_allergens()
        return self.add_allergens_to_food_titles(self.show_menu(), allergens)

    # EXTERNAL method - gets and returns all the customer's past orders in a dictionary
    def view_past_orders(self, customer_id):
        past_order_ids = self.order_data.get_customer(customer_id).get_order_ids()
        all_past_orders = []
        if len(past_order_ids) > 0:
            for order_id in past_order_ids:
                order = self.order_data.get_order(order_id)
                all_past_orders.append({"Order No.":order.order_id, "Dishes":order.dish_names,
                                        "Date":order.date, "Time":order.time})
        return all_past_orders

    # EXTERNAL method - returns the customer details as a dictionary from the instance of the Customer class
    def show_customer_details(self, customer_id):
        return self.order_data.get_customer(customer_id).get_all_details()

    # EXTERNAL method - updates the customer details in the instance of the Customer class
    def update_customer_details(self, customer_id, name="", address="", phone_number=""):
        return self.order_data.get_customer(customer_id).update_customer_details(name, address, phone_number)
    
    # EXTERNAL method - returns a list of the customer's allergens from the instance of the Customer class
    def get_customer_allergens(self, customer_id):
        return self.order_data.get_customer(customer_id).get_allergens()

    # EXTERNAL method - adds new allergens to the list of allergens (in instance of Customer)
    def add_customer_allergens(self, customer_id, allergens):
        new_allergens = []
        for allergen in allergens:
            if allergen not in self.order_data.get_customer(customer_id).get_allergens():
                new_allergens.append(allergen)
        self.order_data.get_customer(customer_id).add_allergens(new_allergens)

    # EXTERNAL method - removes given allergens from the list of allergens (in instance of Customer)
    def remove_customer_allergens(self, customer_id, allergens):
        for allergen in allergens:
            if allergen not in self.order_data.get_customer(customer_id).get_allergens():
                raise Exception("Allergen not found!")
        self.order_data.get_customer(customer_id).remove_allergens(allergens)

    # EXTERNAL method - adds the given dish to the basket in the instance of the Customer class
    def add_dish_to_basket(self, customer_id, dish_title):
        menu_with_allergens = self.show_menu_with_allergens(customer_id)
        index = 0
        for line in menu_with_allergens:
            if line[0] == dish_title:
                index = menu_with_allergens.index(line)
        ordinary_menu = self.show_menu()
        dish = self.menu.get_dish(ordinary_menu[index][0])
        self.order_data.get_customer(customer_id).add_dish(dish)
        return f"{dish_title} was added to your basket."

    # EXTERNAL method - removes the given dish from the basket in the instance of the Customer class
    def remove_dish_from_basket(self, customer_id, dish_title):
        for dish in self.order_data.get_customer(customer_id).get_basket():
            if dish.title in dish_title:
                self.order_data.get_customer(customer_id).remove_dish(dish.title)
                return f"{dish.title} was removed from your basket."
        raise Exception(f"{dish_title} was not in basket!")
    
    # EXTERNAL method - returns a list of dish titles in the customer's basket (from instance of Customer)
    def view_basket(self, customer_id):
        basket = self.order_data.get_customer(customer_id).get_basket()
        basket_list = [[dish.title, f"{dish.calories}cal", f"£{dish.price}"] for dish in basket]
        return self.add_allergens_to_food_titles(basket_list, self.order_data.get_customer(customer_id).get_allergens())

    # EXTERNAL method
    def confirm_order(self, customer_id):
        unique_order_id = self.make_id(999999999999)  # creates order id
        # gives order id to instance of Customer for storing AND gets instances of Dish from Customer
        dishes_ordered = self.order_data.get_customer(customer_id).confirm_order(unique_order_id)
        dish_names = [dish.title for dish in dishes_ordered]  # converts instances of Dish to titles
        date, time = datetime.now().strftime("%d/%m/%Y %H:%M:%S").split()
        # gives the order details to self.order_data (an instance of the OrderData class) which then
        # creates and stores it in an instance of the Order class
        self.order_data.add_order(Order(unique_order_id, customer_id, dish_names, date, time))
        # gets the list of the customer's allergens from the instance of the Customer class
        allergens = self.order_data.get_customer(customer_id).get_allergens()
        # gives the allergens and dish names to self.menu (an instance of the Menu class) which then adds
        # to the number of times each dish has been ordered and adds to the occasion of a customer being
        # allergic to each dish
        self.menu.amend_dish_data(allergens, dish_names)

        return unique_order_id, date, time
