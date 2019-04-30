"""
Jacob Rammer

"""
from typing import List


class Room:

    def __init__(self, windows: bool, balcony: bool, size: int):
        self.windows = windows
        self.balcony = balcony
        self.size = size
        self.available = True

    def __repr__(self):
        return f"Amenities {self.windows} {self.balcony} {self.size} {self.available}"


class RoomSelector:
    def select(self, room: Room) -> bool:

        raise NotImplementedError("No selection method")


class SelectBalconies(RoomSelector):
    def select(self, room: Room) -> bool:
        return room.balcony


class SelectWindows(RoomSelector):
    def select(self, room: Room) -> bool:
        return room.balcony


class Building:

    def __init__(self, rooms: List[Room]):
        self.rooms = rooms
        self.selectors = []
        self.selection = []

    # def add_selector(self, selector, RoomSelector):


    def select(self, f):
        """f should be a boolean function on Room"""

        self.selection = []
        for room in self.rooms:
            for selector in self.selectors:
                if selector.select(room):
                    self.selectors.append(room)
                    break

    def reserve_selected(self):
        for room in self.selection:
            room.available = False

    def print_selected(self):

        for room in self.selection:
            print(repr(room))


deshutes = Building([Room(True, False, 100), Room(False, False, 50), Room(False, False, 30)])
print("Deshutes before selection")
deshutes.print_selected()
deshutes.select(lambda room: room.size >= 50)
deshutes.reserve_selected()
deshutes.select(lambda room: True)
print("Deshutes after reservations")
deshutes.print_selected()
