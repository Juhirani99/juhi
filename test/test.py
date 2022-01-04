@@ -1,9 +1,11 @@
from auction import Auction
from auction_house import AuctionHouse
from item import Item
from participant import Participant
import logging

from auction_system.auction import Auction
from auction_system.auction_house import AuctionHouse
from auction_system.participant import Participant

from auction_system.item import Item

__author__ = "Guillaume Pouilloux <gui.pouilloux@gmail.com>"

logging.getLogger().setLevel(logging.INFO)
