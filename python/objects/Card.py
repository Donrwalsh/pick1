class Card:
    def __init__(self, name, image_uri):
        self.name = name
        self.image_uri = image_uri

    def __repr__(self):
        return "{Card: " + self.name + "}"
