from datetime import datetime


class Set:
    def __init__(self, code, release, count, images=None, diff=None):
        self.code = code
        self.release = datetime.strptime(release, '%Y-%m-%d').date()
        self.count = count
        self.images = images
        self.diff = diff

    def __repr__(self):
        return "{Set: " + self.code + ", " + str(self.release) + ", " + str(self.count) + ", " + \
               str(self.images) + ", " + str(self.diff) + "}"

    def is_complete(self):
        return self.images + self.diff == self.count

    def is_recent(self):
        return self.release.replace(year=self.release.year + 1) > datetime.today().date()

