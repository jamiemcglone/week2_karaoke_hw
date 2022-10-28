import unittest
from classes.guest import Guest
from classes.room import Room


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Jamie", 1000, "Ms. Jackson")
        self.room3 = Room("Super Premium Room", 1, 200)

    def test_guest_has_name(self):
        self.assertEqual("Jamie", self.guest1.name)

    def test_guest_has_cash(self):
        self.assertEqual(1000, self.guest1.cash)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual("Ms. Jackson", self.guest1.favourite_song)

    def test_guest_can_pay(self):
        self.guest1.pay_entrance_fee(self.room3.cost)
        self.assertEqual(800, self.guest1.cash)

    