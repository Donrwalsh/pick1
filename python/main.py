import logging
import os
import scrython

from objects.Set import Set
from services.manifest_service import Manifest


logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger("MAIN")

log.info("Fetching latest set data from scryfall.")
source_sets = []
for set in scrython.sets.Sets().scryfallJson['data']:
     new_set = Set(set['code'], set['released_at'], set['card_count'])
     source_sets.append(new_set)

source_sets.sort(key=lambda x: x.release, reverse=False)

if not Manifest.exists():
    Manifest.generate(source_sets)

manifest_sets = Manifest.read()
exit(0)



