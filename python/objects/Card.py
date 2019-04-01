class Card:
    def __init__(self, name, number, set_code, image_uri, layout):
        self.name = name
        self.number = str(number)
        self.set_code = set_code
        self.image_uri = image_uri
        self.layout = layout

    def __repr__(self):
        return "{Card: " + self.set_code + "-" + self.number + ", [" + self.layout + "] " + self.name + "}"

    def slug(self):
        number = ''.join([i for i in self.number if i.isdigit()])
        leading_zeros = '0' * (3 - len(number))
        return leading_zeros + str(self.number) + "-" +\
            self.name.replace(" ", "-")\
                     .replace(":", "")
