from lib.customer import *
from lib.menu import *
from lib.dish import *
from lib.customer import *
from lib.order_data import *
from lib.order import *
import os
from list_of_animals import animal_list

class TakeawayOrderer:

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

    def create_dish_title(self, animal, dish_title):
        if all(word.isalpha() for word in dish_title.split()):
            return f"{animal.title()} {dish_title}"
        else:
            if any(char=="1" for char in dish_title):
                return f"{dish_title[:-1]} {animal.title()}"
            else:
                return f"{animal.title()} {dish_title[3:]}"

    def match_dish_to_animal(self, menu_data, animal):
        first_letters = 2
        while first_letters > 0:
            for item in menu_data:
                if animal[0:first_letters].lower() == item[0:first_letters].lower():
                    return item
            first_letters -= 1
        raise Exception("Match not found!")
    
    def does_file_exist(self, filename):
        return os.path.isfile(filename)
    
    def get_file_contents(self, filename):
        if self.does_file_exist(filename):
            with open(filename, "r") as file:
                text = file.readlines()
            return [line[:-3] for line in text]
        else:
            return "This file cannot be found!"

    def show_menu(self):
        # gets the menu from the get_formatted_menu() method in the Menu class
        # returns it
        pass

    def add_customer(self, name, allergens, address, phone_number):
        # creates an instance of the Customer class and calls the add_customer(customer) method in the OrderData class
        # returns the customer_id
        pass

    def add_allergens(self, formatted_menu, allergens):
        # returns the formatted menu with the items containing the customers's allergens marked
        pass

    def show_menu_with_allergens(self, customer_id): # CUSTOMER_ID or CUSTOMER CLASS OBJECT ???????
        # gets the menu from the get_formatted_menu() method in the Menu class
        # gets the allergens from the Customer class ???????
        # calls the self.add_allergens(formatted_menu, allergens)
        # prints the menu and marks any dishes the customer will be allergic to
        pass

    def view_past_orders(self, customer_id):
        # gets the customers past order ids and then calls the get_order(order_id) method in the OrderData class for each order id
        # returns all the orders in a formatted message with full details
        pass

    def show_customer_details(self, customer_id):
        # calls the get_all_details() method in the Customer class
        # returns them all in a formatted list for reading
        pass

    def update_customer_details(self, customer_id, name="", address="", phone_number=""):
        # calls the update_customer_details() method in the customer class with the details
        pass
    
    def get_customer_allergens(self, customer_id):
        # calls the get_allergens() method in the Customer class
        # returns them in a list
        pass

    def add_customer_allergens(self, customer_id, allergens):
        # calls the add_allergens(allergens) method in the Customer class to add the allergens
        pass

    def remove_customer_allergens(self, customer_id, allergens):
        # calls the remove_allergens(allergens) method in the Customer class to remove the allergens
        pass

    def add_dish_to_basket(self, customer_id, dish_title):
        # gets the dish from the Menu class from the get_dish(dish_title) method
        # calls the add_dish(dish) method in the Customer class and adds a dish to the customer's basket
        # returns a message saying the dish was successfully added and produces a reminder message if there are any allergens in the dish
        pass

    def remove_dish_from_basket(self, customer_id, dish_title):
        # calls the remove_dish(dish) method in the Customer class and removes the dish from the customer's basket
        # returns a message saying the dish was successfully removed
        pass
    
    def view_basket(self, customer_id):
        # calls the get_basket() method in the Customer class and returns it
        pass

    def confirm_order(self, customer_id):
        # calls the confirm_order(order_id) method in the Customer class and gets the dishes
        # creates an instance of the Order class and calls the add_order(order) method in the OrderData class
        # calls the get_phone_number() method in the Customer class and sends a text message to the customer
        # gets the customer allergens from OrderData using the customer id and calls the amend_dish_data(allergens, dishes) method in the Menu class to add the record of the allergens in the dish and how many times ordered
        pass