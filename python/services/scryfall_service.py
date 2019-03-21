import logging
import pprint
import scrython

from objects.Card import Card
from objects.Set import Set


class Scryfall:
    log = logging.getLogger("SCRYFALL_SERVICE")

    @classmethod
    def generate_setlist(cls):
        output = []
        cls.log.info("Fetching latest set data from scryfall.")
        for set in scrython.sets.Sets().scryfallJson['data']:
            output.append(Set(set['code'], set['released_at'], set['card_count']))
        return output

    @classmethod
    def cards_by_set(cls, set_code, page=1, cards=[]):
        if page == 1:
            cards = []
        query = "e:" + set_code
        response = scrython.cards.Search(q="++{}".format(query), page=page)
        for item in response.data():
            cards.append(Card(item['name'], item['image_uris']['large']))
        if response.has_more():
            return cls.cards_by_set(set_code, page + 1, cards)
        else:
            return cards

    @classmethod
    def download_image(cls, card, path):
        pass
