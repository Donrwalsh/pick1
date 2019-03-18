import scrython
import pprint
import logging
import os
import csv
import time
import datetime

from manifest_service import Manifest

logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
log = logging.getLogger("main")

# fetch 'sets' endpoint

if not Manifest.exists():
    pass
    #create manifest

newer_set = Manifest.Set('lea', '1993-10-22', 250, 250, 0)
new_set = Manifest.Set('leb', '1987-12-22', 250, 250, 0)
third_set = Manifest.Set('3ed', '2000-01-01', 250, 250, 0)
sets = [
    new_set, newer_set, third_set
]
sets.sort(key=lambda x: x.release, reverse=False)

log.info(sets[0].code)
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