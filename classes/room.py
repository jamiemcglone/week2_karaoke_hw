from classes.song import Song
from classes.guest import *

class Room:

    def __init__(self, name, capacity, cost):
        self.name = name
        self.capacity = capacity
        self.cost = cost
        self.room_earnings = 0
        self.guests = []
        self.song_catalogue = [
        Song("Bohemian Rhapsody", "Queen"),
        Song("I Wanna Be Your Lover", "Prince"),
        Song("Everything She Wants", "Wham"),
        Song("High for This", "The Weeknd"),
        Song("I Knew You Were Trouble", "Taylor Swift"),
        Song("Ms. Jackson", "Outkast"),
        Song("Juicy", "The Notorious B.I.G"),
        Song("Heart Shaped Box", "Nirvana"),
        Song("Señorita", "Justin Timberlake")
        ]
        self.song_queue = []

    def add_guest(self, guest):
        if guest not in self.guests and len(self.guests) < self.capacity and guest.cash >= self.cost:
            guest.pay_entrance_fee(self.cost)
            self.room_earnings += self.cost
            self.guests.append(guest)
            self.add_song_to_queue(guest.favourite_song)

    def remove_guest(self, guest):
        self.guests.remove(guest)

    def empty_room(self):
        self.guests.clear()
    
    def add_song_to_catalogue(self, song):
        self.song_catalogue.append(song)
    
    def find_song_by_title(self, title):
        for song in self.song_catalogue:
            if song.title == title:
                return song

    def add_song_to_queue(self, song):
        song_to_add = self.find_song_by_title(song)
        if song_to_add and song_to_add not in self.song_queue:
            self.song_queue.append(song_to_add)
