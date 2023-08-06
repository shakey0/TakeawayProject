import random

all_ids = []
found_repeats = 0
added_ids = 0

def make_id(length):
        found = 0
        added = False
        while True:
            exists = False
            generated_number = str(random.randint(1, length))
            while len(generated_number) < len(str(length)):
                generated_number = "0" + generated_number
            for id in all_ids:
                if id == generated_number:
                    exists = True
                    found += 1
            if not exists:
                added = True
                return generated_number, found, added
            
for _ in range(1000):
    id, found, added = make_id(9999)
    all_ids.append(id)
    print(id)
    found_repeats += found
    if added:
        added_ids += 1
print(found_repeats)
print(added_ids)
            
