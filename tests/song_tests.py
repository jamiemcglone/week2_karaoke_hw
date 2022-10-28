import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Song("Dancing in the Dark", "Bruce Springsteen")
        self.song2 = Song("In Da Club", "50 Cent")
        self.song3 = Song("Someday", "The Strokes")

    def test_song_has_title(self):
        self.assertEqual("Dancing in the Dark", self.song1.title)

    def test_song_has_artist(self):
        self.assertEqual("50 Cent", self.song2.artist)
