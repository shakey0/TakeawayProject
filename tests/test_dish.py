from lib.dish import *

def test_get_times_ordered():
    dish = Dish("Wombat Wonton", 600, 8.49)
    assert dish.get_times_ordered() == 0
    dish.ordered()
    dish.ordered()
    assert dish.get_times_ordered() == 2

def test_get_allergens():
    dish = Dish("Wombat Wonton", 600, 8.49)
    assert dish.get_allergens() == {}
    dish.record_allergens("wo")
    assert dish.get_allergens() == {"wo":1}
    dish.record_allergens("wo")
    assert dish.get_allergens() == {"wo":2}
    dish.record_allergens("wa")
    assert dish.get_allergens() == {"wo":2}
    dish.record_allergens("de")
    dish.record_allergens("nw")
    dish.record_allergens("nt")
    assert dish.get_allergens() == {"wo":2, "nt":1}
    dish.record_allergens("wo")
    dish.record_allergens("nt")
    dish.record_allergens("on")
    assert dish.get_allergens() == {"wo":3, "nt":2, "on":1}