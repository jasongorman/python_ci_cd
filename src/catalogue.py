class Catalogue(object):
    def __init__(self, titles):
        self.titles = titles

    def search(self, artist, title):
        return next(cd for cd in self.titles if cd.artist == artist and cd.title == title)