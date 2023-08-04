class Menu:

    def __init__(self):
        self.all_dishes = []
    
    def add(self, dish):
        self.all_dishes.append(dish)

    def get_dish(self, dish_title):
        for dish in self.all_dishes:
            if dish.title == dish_title:
                return dish
        raise Exception("Dish not in list!")

    def get_most_popular_dishes(self):
        import random
        most_popular_dishes = []
        highest_num = max(dish.times_ordered for dish in self.all_dishes)
        while len(most_popular_dishes) < 5:
            if highest_num == 0:
                return most_popular_dishes
            found_dishes = []
            for dish in self.all_dishes:
                if dish.times_ordered == highest_num:
                    found_dishes.append(dish)
            while len(found_dishes + most_popular_dishes) > 5:
                pop_dish = random.randint(0, len(found_dishes)-1)
                found_dishes.pop(pop_dish)
            most_popular_dishes += found_dishes
            highest_num -= 1
        return most_popular_dishes
            
    def get_formatted_menu(self):
        customer_favourites = self.get_most_popular_dishes()
        formatted_favourites = [f"{dish.title}     {dish.calories}cal     £{dish.price}" for dish in customer_favourites]
        selected_dishes =  [dish for dish in self.all_dishes if dish not in customer_favourites]
        formatted_selected = [f"{dish.title}     {dish.calories}cal     £{dish.price}" for dish in selected_dishes]
        favourites_title = [("-" * 20) + "CUSTOMER FAVOURITES" + ("-" * 20)]
        selected_title = [("-" * 22) + "Selected Dishes" + ("-" * 22)]
        return favourites_title + formatted_favourites + [""] + selected_title + formatted_selected

    def amend_dish_data(self, allergens, dish_names):
        for dish_name in dish_names:
            for dish in self.all_dishes:
                if dish_name == dish.title:
                    dish.ordered()
                    for allergen in allergens:
                        dish.record_allergens(allergen)
