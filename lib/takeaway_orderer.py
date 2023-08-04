from lib.customer import *
from lib.menu import *
from lib.customer import *
from lib.order_data import *

class TakeawayOrderer:

    def __init__(self, menu_csv, animals):
        # creates an instance of the Menu class and assigns it to a variable
        # creates an instance of the OrderData class and assigns it to a variable
        # creates instances of the Dish class with random animals and adds each dish to the Menu class in a for loop
        pass
    
    def add_allergens(self, formatted_menu, allergens):
        # returns the formatted menu with the items containing the customers's allergens marked
        pass

    def show_menu(self, allergens):
        # gets the menu from the get_formatted_menu() method in the Menu class
        # calls the self.add_allergens(formatted_menu, allergens)
        # prints the menu and marks any dishes the customer will be allergic to
        pass

    def add_customer(self, name, allergens, address, phone_number):
        # creates an instance of the Customer class and calls the add_customer(customer) method in the OrderData class
        # returns the customer_id
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