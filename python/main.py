import logging
import os
from datetime import date

from services.manifest_service import Manifest
from services.scryfall_service import Scryfall
from services.images_service import Images

stop_at = date(1994, 10, 6)  # Script will stop after beta
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger("MAIN")

source_sets = Scryfall.generate_setlist()
source_sets.sort(key=lambda x: x.release, reverse=False)

if not Manifest.exists():
    Manifest.generate(source_sets)

manifest_sets = Manifest.read()

for set in manifest_sets:
    if set.release > stop_at:
        log.info(set.code + " is after the stop at value: " + str(stop_at) + ". Terminating.")
        exit(0)

    if set.is_recent():
        log.info(set.code + " is recent.")

    if not set.is_complete():
        log.info(set.code + " is not complete.")
        set_path = Images.set_path(set.code)
        if Images.set_dir_exists(set.code):
            log.info("Found " + set_path + ". Taking no action.")
        else:
            log.info(set_path + " does not exist.")
            Images.create_set_dir(set.code)

        log.info("Fetching complete card list from set: " + set.code + ".")
        data = Scryfall.cards_by_set(set.code)
        data.sort(key=lambda x: x.number, reverse=False)
        for card in data:
            path = Images.image_path(card)
            log.debug("Working on " + str(card))
            if Images.image_exists(card):
                log.debug("Found " + path + ". Taking no action.")
            else:
                log.info(path + " does not exist.")
                Scryfall.download_image(card, path)
                Manifest.record_image_downloaded(set.code, manifest_sets.index(set))
    else:
        log.info(set.code + " is complete.")
