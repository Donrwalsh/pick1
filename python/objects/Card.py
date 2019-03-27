class Card:
    def __init__(self, name, number, set_code, image_uri):
        self.name = name
        self.number = str(number)
        self.set_code = set_code
        self.image_uri = image_uri

    def __repr__(self):
        return "{Card: " + self.set_code + "-" + self.number + ", " + self.name + "}"
