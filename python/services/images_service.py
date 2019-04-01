import logging
import os

class Images:
    log = logging.getLogger("IMAGES_SERVICE")
    images_dir = '../server/src/main/resources/images'

    @classmethod
    def image_path(cls, card):
        return cls.images_dir + "/" + card.set_code + "/" + card.slug() + ".jpeg"

    @classmethod
    def image_exists(cls, card):
        return os.path.exists(cls.image_path(card))

    @classmethod
    def set_dir_exists(cls, set_code):
        return os.path.exists(cls.set_path(set_code))

    @classmethod
    def set_path(cls, set_code):
        return cls.images_dir + "/" + set_code

    @classmethod
    def create_set_dir(cls, set_code):
        cls.log.info("Creating " + set_code + " directory.")
        os.mkdir(cls.set_path(set_code))