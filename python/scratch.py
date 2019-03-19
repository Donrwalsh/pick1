
# Generate Worklist:
# 1. Determine if there is an existing manifest, and if it should be used.
# 2. If not, generate a new worklist and save it as a manifest

for set in scrython.sets.Sets().scryfallJson['data']:
    pprint.pprint(set['released_at'])
    exit(1)


images_dir = '../server/src/main/resources/images'
manifest_file = 'manifest.csv'

# print(os.path.getmtime(manifest_file))
# log.info("last modified: %s" % time.ctime(os.path.getmtime(manifest_file)))
# print("created: %s" % time.ctime(os.path.getctime(manifest_file)))

# create_manifest = not os.path.exists(manifest_file)

print(Manifest.create_manifest())
if Manifest.create_manifest():
    with open(manifest_file, mode='w') as manifest:
        manifest_writer = csv.writer(manifest, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        manifest_writer.writerow(['lea', 150])

# print("last modified: %s" % time.ctime(os.path.getmtime(manifest_file)))
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

newer_set = Manifest.Set('lea', '1993-10-22', 250, 250, 0)
new_set = Manifest.Set('leb', '1987-12-22', 250, 250, 0)
third_set = Manifest.Set('3ed', '2000-01-01', 250, 250, 0)
sets = [
    new_set, newer_set, third_set
]
sets.sort(key=lambda x: x.release, reverse=False)

log.info(sets[0].images)
log.info(sets[1].code)
log.info(sets[2].code)
#
# log.info(new_set.release)
#
# log.info(new_set.is_complete())
#
# a_date = datetime.date(1987, 10, 22)
# log.info(a_date)
#
# another_date = datetime.date(1988, 10, 22)
#
# log.info(a_date >= another_date)
# log.info(datetime.datetime.today().strftime('%Y-%m-%d'))