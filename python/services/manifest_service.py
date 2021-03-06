import os
import csv
import logging
from objects.Set import Set

from services.images_service import Images


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
                manifest_writer.writerow([set.code,
                                          set.release,
                                          set.count,
                                          Images.count_set_images(set.code),
                                          0])

    @classmethod
    def read(cls):
        output = []
        cls.log.info("Reading manifest file: " + cls.manifest_file + ".")
        with open(cls.manifest_file, mode='r') as manifest:
            manifest_reader = csv.reader(manifest)
            for row in manifest_reader:
                output.append(Set(row[0], row[1], row[2], row[3], row[4]))
        return output

    @classmethod
    def get_count(cls, set_code):
        cls.log.debug("Fetching real count from manifest file: " + cls.manifest_file + ".")
        with open(cls.manifest_file, mode="r") as manifest:
            manifest_reader = csv.reader(manifest)
            for row in manifest_reader:
                if row[0] == set_code:
                    return row[3]

    @classmethod
    def record_image_downloaded(cls, set_code):
        cls.log.debug("Modifying manifest: Incrementing " + set_code + " image count.")
        with open(cls.manifest_file, mode='r') as in_manifest:
            manifest_reader = csv.reader(in_manifest.readlines())

        with open(cls.manifest_file, mode="w", newline='') as out_manifest:
            manifest_writer = csv.writer(out_manifest)
            for line in manifest_reader:
                if line[0] == set_code:
                    manifest_writer.writerow([line[0], line[1], line[2], str(int(line[3])+1), line[4]])
                else:
                    manifest_writer.writerow(line)
            manifest_writer.writerows(manifest_reader)

    @classmethod
    def record_diff(cls, set_code, diff):
        cls.log.debug("Modifying manifest: Setting " + set_code + " diff count to " + str(diff) + ".")
        with open(cls.manifest_file, mode='r') as in_manifest:
            manifest_reader = csv.reader(in_manifest.readlines())

        with open(cls.manifest_file, mode="w", newline='') as out_manifest:
            manifest_writer = csv.writer(out_manifest)
            for line in manifest_reader:
                if line[0] == set_code:
                    manifest_writer.writerow([line[0], line[1], line[2], line[3], str(diff)])
                else:
                    manifest_writer.writerow(line)
            manifest_writer.writerows(manifest_reader)