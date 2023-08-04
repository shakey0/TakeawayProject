class Customer:

    def __init__(self, customer_id, name, allergens, address, phone_number):
        self.customer_id = customer_id
        self.name = name
        self.allergens = allergens
        self.address = address
        self.phone_number = phone_number
        self.basket = []
        self.past_order_ids = []

    def get_all_details(self):
        return {"ID Number":self.customer_id, "Name":self.name, "Allergens":self.allergens,
                "Address":self.address, "Phone Number":self.phone_number}

    def update_customer_details(self, name="", address="", phone_number=""):
        if name != "":
            self.name = name
        if address != "":
            self.address = address
        if phone_number != "":
            self.phone_number = phone_number

    def get_allergens(self):
        return self.allergens

    def add_allergens(self, allergens):
        self.allergens += allergens

    def remove_allergens(self, allergens):
        for allergen in allergens:
            self.allergens.remove(allergen)
    
    def get_id(self):
        return self.customer_id
    
    def add_dish(self, dish):
        self.basket.append(dish)

    def remove_dish(self, dish_title):
        count, popped = 0, False
        while count < len(self.basket):
            if self.basket[count].title == dish_title:
                self.basket.pop(count)
                popped = True
                break
            count += 1
        if not popped:
            raise Exception("Dish not found in basket!")
    
    def get_basket(self):
        return self.basket
    
    def confirm_order(self, order_id):
        basket = self.basket
        self.basket = []
        self.past_order_ids.append(order_id)
        return basket

    def get_order_ids(self):
        return self.past_order_ids

    def get_phone_number(self):
        return self.phone_number
