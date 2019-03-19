import logging
import scrython

from objects.Card import Card
from objects.Set import Set


class Scryfall:
    log = logging.getLogger("SCRYFALL_SERVICE")

    layouts = []

    @classmethod
    def generate_setlist(cls):
        output = []
        cls.log.info("Fetching latest set data from scryfall.")
        for set in scrython.sets.Sets().scryfallJson['data']:
            output.append(Set(set['code'], set['released_at'], set['card_count']))
        return output

    @classmethod
    def cards_by_set(cls, code, page, cards):
        query = "e:" + code
        response = scrython.cards.Search(q="++{}".format(query), page=page)
        for item in response.data():
            if item['layout'] not in cls.layouts:
                cls.layouts.append(item['layout'])
            cards.append(Card(item['name']))
        if response.has_more():
            return cls.cards_by_set(code, page+1, cards)
        else:
            return cards

