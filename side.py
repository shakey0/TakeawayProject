from lib.takeaway_orderer import *
from list_of_animals import animal_list

list_of_animals = []
while len(list_of_animals) <= 50:
    animal = animal_list()
    if animal not in list_of_animals:
        list_of_animals.append(animal)

def format_menu(menu):
    all_printed_lines = []
    line_count = 1
    for line in menu:
        if line[0] == "CUSTOMER FAVOURITES" or line[0] == "Selected Dishes" or line[0] == 1:
            printed_line = ""
        else:
            printed_line = f"{line_count}. "
            line_count += 1
        space = [45, 15, 15]
        if line_count > 10:
            space[0] -= 1
        for part, num in zip(line, space):
            if part == 1:
                continue
            else:
                printed_line += part
                leftover = num - len(part)
                printed_line += " " * leftover
        all_printed_lines.append(printed_line)
    return "\n".join(all_printed_lines)

def get_name():
    while True:
        name = input("\nName: ")
        if len(name) <= 30 and name.isalpha():
            return name
        print("\nName can only include letters and be no longer than 30 characters.")

def get_allergens():
    allergens = []
    count = 0
    while True:
        more = "more " if count > 0 else ""
        has_allergens = input(f"\nDo you have any {more}allergens?"
                            "\nY for Yes or N for No: ")
        if has_allergens.lower() == "n":
            return allergens
        elif has_allergens.lower() != "y":
            print("\nInvalid command!")
            continue
        breaker = 0
        while breaker < 2:
            allergen = input("\nType your allergen here: ")
            if len(allergen) == 2 and allergen.isalpha():
                allergens.append(allergen)
                count += 1
                break
            print(f"\nNobody can be allergic to {allergen}!")
            breaker += 1

def get_address():
    while True:
        address = input("\nAddress: ")
        streets = ["street", "road", "drive", "avenue", "boulevard", "close",
                   "crescent", "terrace", "parade", "farm", "courtyard"]
        if 15 <= len(address) <= 50 and any(street in address.lower() for street in streets):
            return address.title()
        print("\nAddress must be between 15 and 50 characters inclusive"
            "\nand include a word that is somewhat of a synonymn with street.")
        
def get_phone_number():
    while True:
        phone_number = input("\nPhone Number (Must be a UK number.): +44")
        if phone_number.isnumeric() and len(phone_number) == 10:
            return int("+44" + phone_number)
        elif phone_number.isnumeric() and len(phone_number) == 11 and phone_number[0] == "0":
            return int("+44" + phone_number[1:])
        print("\nInvalid UK phone number.")

def get_customer_details():
    name = get_name()
    allergens = get_allergens()
    address = get_address()
    phone_number = get_phone_number()
    return name, allergens, address, phone_number

def get_choice(choices, other):
    while True:
        choice = input(f"\nChoose from the {len(choices)} options above: ")
        if choice in choices or choice.lower() in other:
            return choice
        print("\nInvalid command!")

def option1(customer_id):
    while True:
        menu = takeaway_orderer.show_menu_with_allergens(customer_id)
        print(format_menu(menu))
        avoid_list = ["CUSTOMER FAVOURITES", "Selected Dishes", 1]
        listed_items = [line[0] for line in menu if line[0] not in avoid_list]
        print("\nTo add items press the item number + Enter."
              "\nPress B + Enter to view your basket.")
        option = get_choice([str(num) for num in range(1, 16)], ["q", "b"])
        if option == "q":
            break
        elif option == "b":
            pass  # VIEW BASKET !!!!!!!
        print("\n" + takeaway_orderer.add_dish_to_basket(customer_id, listed_items[int(option)-1]))
        break

def while_logged_in(customer_id):
    while True:
        print("\nOPTIONS:\n1. See Menu & Order\n2. View Past Orders\n3. Your Details\n4. Review Allergens"
              "\n5. Go to Basket\n6. Sign Out")
        option = get_choice(["1", "2", "3", "4", "5", "6"], ["q"])
        if option == "q":
            break
        if option == "1":
            option1(customer_id)
        break


takeaway_orderer = TakeawayOrderer("menu.csv", list_of_animals)
print(format_menu(takeaway_orderer.show_menu()))
input("\nPress Enter to continue.")
name, allergens, address, phone_number = get_customer_details()
customer_id = takeaway_orderer.add_customer(name, allergens, address, phone_number)
print(f"\nYour customer ID is: {customer_id}")
print("\nYou have been automatically logged in.")
while_logged_in(customer_id)