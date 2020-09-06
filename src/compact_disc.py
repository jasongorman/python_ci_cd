class CompactDisc(object):
    def __init__(self, artist, title, price, stock, payments):
        self.title = title
        self.artist = artist
        self.price = price
        self.payments = payments
        self.stock = stock

    def buy(self, quantity, card):
        if self.payments.pay(self.price, card):
            self.stock -= quantity

