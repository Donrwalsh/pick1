import os
import csv
import logging

class Manifest:
    log = logging.getLogger("manifest service")
    manifest_file = 'manifest.csv'

    @classmethod
    def create_manifest(cls):
        if cls.manifest_exists():
            return cls.manifest_is_valid()
        return False

    @classmethod
    def manifest_exists(cls):
        if os.path.exists(cls.manifest_file):
            cls.log.info("Manifest file " + cls.manifest_file + " exists.")
            return True
        cls.log.info("Manifest file " + cls.manifest_file + " does not exist.")
        return False

    @classmethod
    def manifest_is_valid(cls):
        with open(cls.manifest_file, mode='r') as manifest:
            cls.log.info("Reading manifest from " + cls.manifest_file + ":")
            row_count = 0
            manifest_reader = csv.reader(manifest)
            for row in manifest_reader:
                row_count += 1
                cls.log.info("Validating row " + str(row_count) +
                             ". Found values: " + row[0] + ", " + str(row[1]) + ".")
                if isinstance(row[1], (int)):
                    return False
        return True


    # how long since update?