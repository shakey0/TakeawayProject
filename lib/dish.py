class Dish:

    def __init__(self, title, calories, price):
        self.title = title
        self.calories = calories
        self.price = price
        self.times_ordered = 0
        self.allergens_in_dish = {}

    def ordered(self):
        self.times_ordered += 1
    
    def get_times_ordered(self):
        return self.times_ordered

    def record_allergens(self, allergen):
        if allergen in self.title.lower():
            if allergen in self.allergens_in_dish.keys():
                self.allergens_in_dish[allergen] += 1
            else:
                self.allergens_in_dish[allergen] = 1

    def get_allergens(self):
        return self.allergens_in_dish
