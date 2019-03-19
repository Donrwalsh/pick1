import logging
import scrython

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
