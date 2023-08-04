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

    def get_id(self):
        # returns the customer's unique id
        pass

    def get_allergens(self):
        # returns the customer's allergens
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

    def get_phone_number(self):
        # returns the customer's phone number from the __init__ class
        pass
