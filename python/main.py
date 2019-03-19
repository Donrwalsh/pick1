import logging
import os

from services.manifest_service import Manifest
from services.scryfall_service import Scryfall

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger("MAIN")
images_dir = '../server/src/main/resources/images'


source_sets = Scryfall.generate_setlist()
source_sets.sort(key=lambda x: x.release, reverse=False)

if not Manifest.exists():
    Manifest.generate(source_sets)

manifest_sets = Manifest.read()

for set in manifest_sets:
    if set.is_recent():
        log.info(set.code + " is recent.")

    if not set.is_complete():
        log.info(set.code + " is not complete.")
        log.info("Fetching complete card list from set: " + set.code)
        data = Scryfall.cards_by_set(set.code, 1, [])
        for card in data:
            log.info("Working on [" + set.code + "] " + card.name)
            #does card image exist on filesystem?
            #if no, download image and modify manifest.

exit(0)
