word = "hello world"

if all(word.isalpha() for word in word.split()):
    print("Yes")
else:
    print("No")

dish_row = "Ginger Snaps;580;6.99;"

dish_info = dish_row.split(";")[:-1]

print(dish_info)

from list_of_animals import animal_list

animals = []
for _ in range(15):
    animals.append(animal_list())
print(animals)