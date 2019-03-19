import os
import csv
import logging
from objects.Set import Set


class Manifest:
    log = logging.getLogger("MANIFEST_SERVICE")
    manifest_file = 'manifest.csv'

    @classmethod
    def exists(cls):
        if os.path.exists(cls.manifest_file):
            cls.log.info("Manifest file " + cls.manifest_file + " exists.")
            return True
        cls.log.info("Manifest file " + cls.manifest_file + " does not exist.")
        return False

    @classmethod
    def generate(cls, source):
        cls.log.info("Manifest file will be created as: " + cls.manifest_file)
        with open(cls.manifest_file, mode='w', newline='') as manifest:
            manifest_writer = csv.writer(manifest, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for set in source:
                manifest_writer.writerow([set.code, set.release, set.count, 0, 0])

    @classmethod
    def read(cls):
        output = []
        cls.log.info("Reading manifest file: " + cls.manifest_file + ".")
        with open(cls.manifest_file, mode='r') as manifest:
            manifest_reader = csv.reader(manifest)
            for row in manifest_reader:
                output.append(Set(row[0], row[1], row[2], row[3], row[4]))
        return output


