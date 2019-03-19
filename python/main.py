import logging
import os

from services.manifest_service import Manifest
from services.scryfall_service import Scryfall

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger("MAIN")

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


exit(0)



