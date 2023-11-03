# Takeaway Orderer Project

## Introduction
This is a project that I really went nuts on and did so many things with. The project has many features and parts to it. See Part 1 in [recipe.md](recipe.md) for the initial requirements of which I went far beyond. Part 2 in [recipe.md](recipe.md) shows my planning of the class system.

## Features

Upon running the app, 50 animals are chosen from the animal list in [list_of_animals.py](list_of_animals.py) . This list of animals along with the [menu.csv](menu.csv) are then parsed to the TakeawayOrderer class upon initialisation (see [takeaway_orderer.py](lib/takeaway_orderer.py)). During the init process for this class, 15 of these animals are then taken and matched with dishes from [menu.csv](menu.csv) according to their first 2 letters or first letter.
- This ensures that each time the app is run, a new amusing set of animals are matched with dish names.
- This menu is now used until the running of the app is terminated.
- (If you want a quick rundown of what the code in [takeaway_orderer.py](lib/takeaway_orderer.py) is doing, copy and paste it into ChatGPT.)
- Below are 2 examples of different randomly generated menus.

<p align="center">
    <img alt="Menu example 1" src="assets/menu_example_1.png" width="45%"/>
    <img alt="Menu example 2" src="assets/menu_example_2.png" width="45%"/>
</p>

The user enters their details, essentially creating some kind of account.
- name, address, **allergens**, phone numbers
- The **allergens** here are something I spent a lot of time on.
    - An allergen in this app is any 2 letters of the alphabet together (ox, er, pl, oa, ii), the customer chooses this.
    - Customers can choose from 0 to as many allergens as they like.
    - The allergens are stored in a list in the instance of the Customer class.
    - Each time the menu is printed, any dishes containing the 2 consecutive letters of the allergen will have a message next to it.
    - (If you want to see the code for this, look at the 'add_allergens_to_food_titles' method in [takeaway_orderer.py](lib/takeaway_orderer.py) .)
    - Below is an example of how the allergen warning messages are added.

![Allergens example](assets/allergens_example.png)

Once the user has entered their details, the main menu will be shown. This menu has 6 options:
1. **See Menu & Order** (Upon pressing '1' + 'Enter' the menu with any allergens are displayed. The user can then add dished to their basket from here. <em>To go back to the main menu from here press 'Q' + 'Enter'.</em>)
2. **View Past Orders** (Upon pressing '2' + 'Enter' the user's pasts orders are shown.)
3. **Your Details** (Upon pressing '3' + 'Enter' the user's details are shown. The user can then amend any of their details.)
4. **Review Allergens** (Upon pressing '4' + 'Enter' the user's allergens are shown. The user can then remove or add allergens. Next time the menu is shown, these changes are reflected.)
5. **Go to Basket** (Upon pressing '5' + 'Enter' the user can see their basket. If it's got any items in it, they can choose to place their order by pressing 'C' + 'Enter'.)
6. **Sign Out** (Upon pressing '6' + 'Enter' the app will terminate.)

Below is an example of when a customer places an order and the message they get confirming their order.

![Place order example](assets/place_order_example.png)

Below is an example of option 2 'View Past Orders'. You can see the **datetime module** being used here when a user places an order. A **random order number** is generated too.

![Past orders example](assets/past_orders_example.png)

One more thing I've included in this app is **Customer Favourites**.
- The app keeps track of how many times each item is ordered and it uses this to add them to the top 5 dishes.
- (If you want to see the code for this, look at the 'get_most_popular_dishes' method in [menu.py](lib/menu.py) .)
- Below is an example of this. (You can see that these dishes are in the previous example too.)

![Customer favourites example](assets/customer_favourites_example.png)

## Installation & Setup

Run the following command to clone the repo:
```bash
git clone https://github.com/shakey0/TakeawayProject
cd TakeawayProject
```

Create your virtual environment:
```bash
pipenv install
```

Run the tests:
```bash
pytest
```

Start the app: (I didn't finished the CLI, but did start it, so you can get a basic idea of how things work.)
```bash
python app.py
```