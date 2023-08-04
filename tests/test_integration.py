from lib.takeaway_orderer import *
from lib.customer import *
from lib.menu import *
from lib.dish import *
from lib.order_data import *
from lib.order import *

def test_takeaway_orderer_init():
    takeaway_orderer = TakeawayOrderer("menu.csv", ['Mouse', 'Whale', 'Anteater', 'Pig', 'Albatross',
                                                    'Vulture', 'Human', 'Mongoose', 'Scorpion', 'Badger',
                                                    'Oyster', 'Okapi', 'Termite', 'Nightingale', 'Eagle'])
    assert len(takeaway_orderer.menu.all_dishes) == 15
    assert takeaway_orderer.menu.all_dishes[1].title == "Whale Wonton"
    assert takeaway_orderer.menu.all_dishes[8].price == 7.49
    assert takeaway_orderer.menu.all_dishes[11].calories == 420

