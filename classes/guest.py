class Guest:

    def __init__(self, name, cash, favourite_song):
        self.name = name
        self.cash = cash
        self.favourite_song = favourite_song

    def pay_entrance_fee(self, room_fee):
        self.cash -= room_fee