import scrython
import pprint
import logging
import os
import csv
import time

from manifest_service import Manifest

logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
log = logging.getLogger("main")

# Generate Worklist:
# 1. Determine if there is an existing manifest, and if it should be used.
# 2. If not, generate a new worklist and save it as a manifest




images_dir = '../server/src/main/resources/images'
manifest_file = 'manifest.csv'

# print(os.path.getmtime(manifest_file))
# log.info("last modified: %s" % time.ctime(os.path.getmtime(manifest_file)))
# print("created: %s" % time.ctime(os.path.getctime(manifest_file)))

create_manifest = not os.path.exists(manifest_file)

print(Manifest.create_manifest())
if Manifest.create_manifest():
    with open(manifest_file, mode='w') as manifest:
        manifest_writer = csv.writer(manifest, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        manifest_writer.writerow(['lea', 150])

print("last modified: %s" % time.ctime(os.path.getmtime(manifest_file)))
exit(1)


log.info("Constructing list of existing image folders")
log.debug("Using images_dir: " + images_dir)

folders = []
for dir in os.listdir('../server/src/main/resources/images'):
    if dir not in ['.DS_Store', 'templates', 'application.properties']:
        folders.append([dir, len(os.listdir('../server/src/main/resources/images/' + dir))])

log.info("Fetching list of all sets from Scryfall")
worklist = []


for set in scrython.sets.Sets().scryfallJson['data']:
    log.debug("Fetching card count for " + set['code'])
    query = "e:" + set['code']
    cards = scrython.cards.Search(q="++{}".format("e:" + set['code'])).data()
    worklist.append([set['code'], len(cards)])


for exists in folders:
    try:
        worklist.remove(exists)
    except ValueError:
        pass

pprint.pprint('Remaining Sets:')

worklist.sort()
pprint.pprint(worklist)
