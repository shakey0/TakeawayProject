from lib.takeaway_orderer import *
from list_of_animals import animal_list

list_of_animals = []
while len(list_of_animals) <= 50:
    animal = animal_list()
    if animal not in list_of_animals:
        list_of_animals.append(animal)

def format_menu(menu):
    all_printed_lines = []
    for line in menu:
        printed_line = ""
        for part in line:
            if part == 1:
                printed_line += " " * 25
            else:
                printed_line += part
                leftover = 25 - len(part)
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
        more = "more" if count > 0 else ""
        has_allergens = input(f"\nDo you have any {more} allergens?"
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
        address = input("\Address: ")
        streets = ["street", "road", "drive", "avenue", "boulevard", "close",
                   "crescent", "terrace", "parade", "farm", "courtyard"]
        if 15 <= len(address) <= 50 and any(street in address.lower() for street in streets):
            return address.title()
        print("\nAddress must be between 15 and 50 characters inclusive"
            "\nand include a word that is somewhat of a synonymn with street.")

def get_customer_details():
    
    
    while True


takeaway_orderer = TakeawayOrderer("menu.csv", list_of_animals)
print(format_menu(takeaway_orderer.show_menu()))
