import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("room1", 5, 0)
        self.room2 = Room("room2", 10, 3)
        self.room3 = Room("Super Premium Room", 1, 200)
        self.song1 = Song("Dancing in the Dark", "Bruce Springsteen")
        self.song2 = Song("In Da Club", "50 Cent")
        self.song3 = Song("Someday", "The Strokes")
        self.guest1 = Guest("Jamie", 1000, "Ms. Jackson")
        self.guest2 = Guest("Bob", 5, "Bohemian Rhapsody")
        self.guest3 = Guest("Fred", 10, "High for This")
        self.guest4 = Guest("Frank", 20, "Juicy")
        self.guest5 = Guest("Jim", 50, "Everything She Wants")
        self.guest6 = Guest("Woody", 75, "I Knew You Were Trouble")

    def test_room_has_name(self):
        self.assertEqual("room1", self.room1.name)
    
    def test_room_has_capacity(self):
        self.assertEqual(5, self.room1.capacity)
    
    def test_room_has_cost(self):
        self.assertEqual(200, self.room3.cost)

    def test_room_starts_empty(self):
        self.assertEqual(0, len(self.room2.guests))

    def test_can_add_guest_to_room(self):
        self.room2.add_guest(self.guest2)
        self.assertEqual(1, len(self.room2.guests))
        self.assertEqual(2, self.guest2.cash)
        self.assertEqual(3, self.room2.room_earnings)
        self.assertEqual("Bohemian Rhapsody", self.room2.song_queue[0].title)
    
    def test_can_add_guest_to_room_refuses_duplicates(self):
        self.room2.add_guest(self.guest2)
        self.room2.add_guest(self.guest2)
        self.assertEqual(1, len(self.room2.guests))

    def test_add_guest_to_room_refuses_as_over_capacity(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)
        self.room1.add_guest(self.guest3)
        self.room1.add_guest(self.guest4)
        self.room1.add_guest(self.guest5)
        self.room1.add_guest(self.guest6)
        self.assertEqual(5, len(self.room1.guests))
        
    def test_can_remove_guest_from_room(self):
        self.room2.add_guest(self.guest1)
        self.room2.add_guest(self.guest2)
        self.room2.remove_guest(self.guest2)
        self.assertEqual(1, len(self.room2.guests))

    def test_clear_room(self):
        self.room2.add_guest(self.guest1)
        self.room2.add_guest(self.guest2)
        self.assertEqual(2, len(self.room2.guests))
        self.room2.empty_room()
        self.assertEqual(0, len(self.room2.guests))

    def test_rooms_have_catalogue(self):
        self.assertEqual(9, len(self.room1.song_catalogue))
        self.assertEqual(9, len(self.room2.song_catalogue))

    def test_can_add_to_catalogue(self):
        self.room1.add_song_to_catalogue(self.song1)
        self.room2.add_song_to_catalogue(self.song2)
        self.assertEqual(10, len(self.room1.song_catalogue))
        self.assertEqual(10, len(self.room2.song_catalogue))

    def test_room_song_queue_starts_empty(self):
        self.assertEqual(0, len(self.room2.song_queue))

    def test_can_add_song_to_queue(self):
        self.room1.add_song_to_queue("I Knew You Were Trouble")
        self.room1.add_song_to_queue("Ms. Jackson")
        self.room1.add_song_to_queue("Juicy")
        self.assertEqual(3, len(self.room1.song_queue))

    def test_add_song_to_queue_not_in_catalogue(self):
        self.room2.add_song_to_queue("As It Was")
        self.assertEqual(0, len(self.room2.song_queue))

    def test_add_song_to_queue_does_not_allow_duplicates(self):
        self.room1.add_song_to_queue("Everything She Wants")
        self.room1.add_song_to_queue("Everything She Wants")
        self.assertEqual(1, len(self.room1.song_queue))
