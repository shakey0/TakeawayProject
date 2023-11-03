from lib.takeaway_orderer import *
from list_of_animals import animal_list

list_of_animals = []
while len(list_of_animals) <= 50:
    animal = animal_list()
    if animal not in list_of_animals:
        list_of_animals.append(animal)

def format_list(menu):
    all_printed_lines = []
    line_count = 1
    print("")
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

def print_allergens_list(allergens, space=True):
    current_allergens = ", ".join(allergens) if len(allergens) > 0 else "None"
    if space:
        print("")
    print(f"ALLERGENS: {current_allergens}")

def get_allergens(allergens=[]):
    print("\nAllergens in this world are 2 consecutive letters of the alphabet."
          "\nFor example, 'rq', 're', 'tt', 'oa', etc.")
    while True:
        print_allergens_list(allergens)
        more = "more " if len(allergens) > 0 else ""
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
                break
            print(f"\nNobody can be allergic to {allergen}!")
            breaker += 1

def get_address():
    while True:
        address = input("\nAddress: ")
        if 5 <= len(address) <= 50:
            return address.title()
        print("\nAddress must be between 5 and 50 characters inclusive.")
        
def get_phone_number():
    while True:
        phone_number = input("\nPhone Number (Must be a UK number.): +44")
        if phone_number.isnumeric() and len(phone_number) == 10:
            return "+44" + phone_number
        elif phone_number.isnumeric() and len(phone_number) == 11 and phone_number[0] == "0":
            return "+44" + phone_number[1:]
        print("\nInvalid UK phone number.")

def get_customer_details():
    name = get_name()
    allergens = get_allergens()
    address = get_address()
    phone_number = get_phone_number()
    return name, allergens, address, phone_number

def get_choice(number_choices, letter_choices):
    while True:
        choice = input(f"\nChoose from the options above:\n")
        if choice in number_choices or choice.lower() in letter_choices:
            return choice
        print("\nInvalid command!")

def place_order(customer_id):
    order_number, date, time = takeaway_orderer.confirm_order(customer_id)
    print("\nYour order has been successfully placed."
        f"\nDATE: {date}     TIME: {time}     ORDER NO: {order_number}"
        f"\nIt will be delivered to {takeaway_orderer.show_customer_details(customer_id)['Address']}."
        "\nThank you for your order!")
    input("\nPress Enter to continue.\n")

def option5(customer_id):
    basket = takeaway_orderer.view_basket(customer_id)
    print("\nYOUR BASKET")
    if len(basket) == 0:
        print("Your basket is empty.")
        input("\nPress Enter to go back.\n")
        return True
    print(format_list(basket))
    while True:
        choice = input("\nPress C + Enter to place your order."
                        "\nPress B + Enter to go back.\n")
        choice = choice.lower()
        if choice == "c":
            place_order(customer_id)
            return False
        elif choice == "b":
            return True
        else:
            print("\nInvalid command!")

def option1(customer_id):
    while True:
        menu = takeaway_orderer.show_menu_with_allergens(customer_id)
        print(format_list(menu))
        avoid_list = ["CUSTOMER FAVOURITES", "Selected Dishes", 1]
        listed_items = [line[0] for line in menu if line[0] not in avoid_list]
        print("\nTo add items press the item number + Enter."
                "\nPress B + Enter to view your basket.")
        option = get_choice([str(num) for num in range(1, 16)], ["q", "b"])
        if option.lower() == "q":
            break
        elif option.lower() == "b":
            command = option5(customer_id)
            if command:
                print(format_list(menu))
            else:
                break
        elif option in [str(num) for num in range(1, 16)]:
            print("\n" + takeaway_orderer.add_dish_to_basket(customer_id, listed_items[int(option)-1]))
            input("\nPress Enter to continue.")
        else:
            print("\nInvalid command!")

def option2(customer_id):
    orders = takeaway_orderer.view_past_orders(customer_id)
    if len(orders) == 0:
        print("\nYou haven't made any orders yet!")
    for order in orders:
        print(f"\nORDER NO: {order['Order No.']}"
            f"\nCONTENTS: {', '.join(order['Dishes'])}"
            f"\nDATE: {order['Date']}     TIME: {order['Time']}")
    input("\nPress Enter to go back.\n")

def print_customer_details(details):
    print(f"\nCUSTOMER ID: {details['ID Number']}"
        f"\nName: {details['Name']}"
        f"\nAddress: {details['Address']}"
        f"\nPhone Number: {details['Phone Number']}")
    allergens = takeaway_orderer.get_customer_allergens(customer_id)
    print_allergens_list(allergens, space=False)

def remove_allergens(customer_id):
    count = 0
    while True:
        to_remove = input("\nAllergen to remove: ")
        if to_remove in takeaway_orderer.get_customer_allergens(customer_id):
            takeaway_orderer.remove_customer_allergens(customer_id, [to_remove])
            print("\nAllergen removed.")
            break
        else:
            print("\nAllergen not found!")
        count +=1
        if count == 3:
            break

def option4(customer_id):
    while True:
        allergens = takeaway_orderer.get_customer_allergens(customer_id)
        print_allergens_list(allergens)
        print("\nA = Add Allergen(s)\nR = Remove Allergen(s)\nB = Back to Previous Section")
        choices = ["a", "r", "b"]
        option = get_choice([], choices)
        if option == "a":
            new_allergens = get_allergens(allergens)
            if len(new_allergens) > 0:
                takeaway_orderer.add_customer_allergens(customer_id, new_allergens)
                print("\nYour allergens were updated.\n")
        elif option == "r":
            if len(allergens) == 0:
                print("\nYou don't have any allergens recorded!")
                input("\nPress Enter to continue.\n")
                continue
            remove_allergens(customer_id)
            input("\nPress Enter to continue.\n")
        elif option == "b":
            break

def option3(customer_id):
    while True:
        details = takeaway_orderer.show_customer_details(customer_id)
        print_customer_details(details)
        print("\nN = Amend Name\nX = Amend Allergens\nA = Amend Address\nP = Amend Phone Number\nB = Back")
        choices = ["n", "x", "a", "p", "b"]
        option = get_choice([], choices)
        if option == "n":
            name = get_name()
            takeaway_orderer.update_customer_details(customer_id, name=name)
            input("\nPress Enter to continue.\n")
        elif option == "x":
            option4(customer_id)
        elif option == "a":
            address = get_address()
            takeaway_orderer.update_customer_details(customer_id, address=address)
            input("\nPress Enter to continue.\n")
        elif option == "p":
            phone_number = get_phone_number()
            takeaway_orderer.update_customer_details(customer_id, phone_number=phone_number)
            input("\nPress Enter to continue.\n")
        else:
            break

def while_logged_in(customer_id):
    while True:
        print("\nOPTIONS:\n1. See Menu & Order\n2. View Past Orders\n3. Your Details\n4. Review Allergens"
            "\n5. Go to Basket\n6. Sign Out")
        option = get_choice(["1", "2", "3", "4", "5", "6"], ["q"])
        if option.lower() == "q":
            break
        elif option == "1":
            option1(customer_id)
        elif option == "2":
            option2(customer_id)
        elif option == "3":
            option3(customer_id)
        elif option == "4":
            option4(customer_id)
        elif option == "5":
            option5(customer_id)
        else:
            break


takeaway_orderer = TakeawayOrderer("menu.csv", list_of_animals)
print(format_list(takeaway_orderer.show_menu()))
input("\nPress Enter to continue.\n")
name, allergens, address, phone_number = get_customer_details()
customer_id = takeaway_orderer.add_customer(name, allergens, address, phone_number)
print(f"\nYour customer ID is: {customer_id}")
print("\nYou have been automatically logged in.")
while_logged_in(customer_id)