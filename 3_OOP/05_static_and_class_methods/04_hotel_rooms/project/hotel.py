
from project.room import Room

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)
        return self.rooms

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.take_room(people)  # no need to repeat room logic

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.free_room()

    def status(self):
        free_rooms = ", ".join([str(r.number) for r in self.rooms if not r.is_taken])
        taken_rooms = ", ".join([str(r.number) for r in self.rooms if r.is_taken])
        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {free_rooms}\nTaken rooms: {taken_rooms}"
