## 1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.


## 2. Design the Class System

TakeawayOrderer: (Main Class)

```python
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
        # gets the customer allergens from OrderData using the customer id and calls the amend_dish_data(allergens, dish_names) method in the Menu class to add the record of the allergens in the dish and how many times ordered
        pass


class Menu:

    def __init__(self):
        # - stores a list of dishes (instances of the Dish class)
        pass
    
    def add(self, dish):
        # adds an instance of the dish class to the list in the __init__ method
        pass

    def get_dish(self, dish_title):
        # returns the dish according to the title
        # raises an error if the title can't be found
        pass

    def get_most_popular_dishes(self):
        # goes through the list of dishes and finds the 5 most popular dishes as long as the time of orders are greater than 1, if ties reach more than 5, random selections will be made from the ties
        pass

    def get_formatted_menu(self):
        # returns the menu in a formatted form, also uses the get_most_popular_dish() method to add the most popular items to the top
        pass

    def amend_dish_data(self, allergens, dish_names):
        # finds the dish in the list of dishes to add the record of the allergens in the dish and how many times ordered
        pass


class Dish:

    def __init__(self, title, calories, price):
        # stores the title
        # stores the calories
        # stores the price
        # - stores a number representing the number of times the dish has been ordered
        # - stores a dictionary of allergens and how many times a customer has been allergic to them
        pass
    
    def ordered(self):
        # adds 1 to the number of how many times the dish has been ordered
        pass
    
    def get_times_ordered(self):
        # returns the number of times the dish has been ordered
        pass

    def record_allergens(self, allergen):
        # adds the allergen (if any) to the dictionary in the __init__ method (adds one to the value if the allergen already exists)
        pass

    def get_allergens(self):
        # returns the dictionary of allergens from the __init__ method
        pass


class OrderData:

    def __init__(self):
        # stores a list of customers (instances of the Customer class)
        # stores a list of orders (instances of the Order class)
        pass

    def add_customer(self, customer):
        # adds an instance of the Customer class to the list in the __init__ method
        pass
    
    def get_customer(self, customer_id):
        # returns relevant customer (if exists) from the list in the __init__ method
        pass

    def add_order(self, order):
        # adds an instance of the Order class to the list in the __init__ method 
        pass
    
    def get_order(self, order_id):
        # returns relevant order (if exists) from the list in the __init__ method
        pass


class Order:

    def __init__(self, order_id, customer_id, dish_names, date, time):
        # stores all the values passed in in unique variables
        pass
    

class Customer:

    def __init__(self, customer_id, name, allergens, address, phone_number):
        # stores the customer's unique id
        # stores the customer's name
        # stores the customer's allergens
        # stores the customer's address
        # stores the customer's phone_number
        # - stores a list of the dishes in the customer's basket (instances of the Dish class)
        # - stores a list of the customer's past order ids
        pass
    
    def get_all_details(self):
        # returns all the customers details in a dictionary
        pass

    def update_customer_details(self, name="", address="", phone_number=""):
        # updates the customer's name, address and/or phone number
        pass

    def get_allergens(self):
        # returns the customer's allergens
        pass

    def add_allergens(self, allergens):
        # adds new allergens to the list in the __init__ method
        pass

    def remove_allergens(self, allergens):
        # removes allergens from the list in the __init__ method
        pass
    
    def get_id(self):
        # returns the customer's unique id
        pass

    def add_dish(self, dish):
        # adds the dish (an instance of the class Dish) to the list of stored dishes in the __init__ method (the customer's basket)
        pass

    def remove_dish(self, dish_title):
        # removes the dish from the list of stored dishes in the __init__ method
        pass
    
    def get_basket(self):
        # returns the customer's basket (a list) from the list of stored dishes in the __init__ method
        pass
    
    def confirm_order(self, order_id):
        # empties the list of the dishes in the customer's basket
        # adds the order id to the customer's past order ids in the __init__ method
        # returns all the contents of the customer's baskets in a list
        pass
    
    def get_order_ids(self):
        # returns the customer's past order ids
        pass

    def get_phone_number(self):
        # returns the customer's phone number from the __init__ class
        pass
