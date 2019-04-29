"""
Jacob Rammer
sdk_board.py for sudoku
"""

from sdk_config import CHOICES, UNKNOWN, ROOT
from sdk_config import NROWS, NCOLS
import logging
import enum
from typing import List, Sequence, Set

"""
A Sudoku board holds a matrix of tiles.
Each row and column and also sub-blocks
are treated as a group (sometimes called
a 'nonet'); when solved, each group must contain
exactly one occurrence of each of the
symbol choices.
"""

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)  # .info of low level of verbosity


# --------------------------------
#  The events for MVC
# --------------------------------

class Event(object):
    """
    Abstract base class of all events, both for MVC
    and for other purposes
    """

    pass


# --------------------------------
#  Listeners (base class)
# --------------------------------

class Listener(object):
    """
    Abstract base class for listeners.
    Subclass this to make the notification do
    something useful.
    """

    def __init__(self):
        """Default contructor for simple listeners without state"""

        pass

    def notify(self, event: Event):
        """
        The 'notify' method of the base class must be
        overridden in concrete classes.
        """

        raise NotImplementedError("You must override Listener.notify")


# --------------------------------------
#  Events and listeners for Tile Objects
# --------------------------------------

class EventKind(enum.Enum):
    TileChanged = 1
    TileGuessed = 2


class TileEvent(Event):
    """
        Abstract base class for things that happen to tiles.
        We always indicate the tile. Concrete subclasses indicate
        the nature of the event.
        """

    def __init__(self, tile: "Tile", kind: EventKind):
        self.tile = tile
        self.kind = kind

        """
        Note: "Tile" type is a forward reference.
        Tile class is defined below.
        """

    def __str__(self):
        """
        Printed representation includes name of concrete subclass
        """

        return f"{repr(self.tile)}"


class TileListener(Listener):

    def notify(self, event: Event):
        raise NotImplementedError("TileListener subclass needs to override notify(TileEvent)")


class Listenable:
    """
    Objects to which listeners (like view component) can be attached
    """

    def __init__(self):
        self.listeners = []

    def add_listener(self, listener: Listener):
        self.listeners.append(listener)

    def notify_all(self, event: Event):
        for listener in self.listeners:
            listener.notify(event)


class Tile(Listenable):
    """
    One tile on the Sudoku grid.
    Public attributes (read-only): value, which will be either
    UNKNOWN or an element of CHOICES; candidates, which will
    be a set drawn from CHOICES. If value is an element of
    CHOICES, then candidates will be the singleton containing
    value. If candidates is empty, then no tile value can
    be consistent with other tile values in the grid.
    Value is a public read-only attribute; change it
    only through the access method set_value or indirectly
    through method remove_candidates.
    """

    def __init__(self, row: int, col: int, value=UNKNOWN):
        super().__init__()
        assert value == UNKNOWN or value in CHOICES
        self.row = row
        self.col = col
        self.set_value(value)

    def set_value(self, value: str):

        if value in CHOICES:
            self.value = value
            self.candidates = {value}
        else:
            self.value = UNKNOWN
            self.candidates = set(CHOICES)
            self.notify_all((TileEvent(self, EventKind.TileChanged)))

    def __str__(self) -> str:
        """
        Return the value of the Tile
        """

        return f"{self.value}"

    def __repr__(self) -> str:
        """
        Return the representation of a tile with row
        """

        return f"Tile({self.row}, {self.col}, '{self.value}')"

    def could_be(self, value: str) -> bool:
        """
        True iff value is a candidate value for this tile
        """

        return value in self.candidates

    def remove_candidates(self, used_values: Set[str]):
        """The used values cannot be a value of this unknown tile.
        We remove those possibilities from the list of candidates.
        If there is exactly one candidate left, we set the
        value of the tile.
        Returns:  True means we eliminated at least one candidate,
        False means nothing changed (none of the 'used_values' was
        in our candidates set).
        """
        new_candidates = self.candidates.difference(used_values)
        if new_candidates == self.candidates:
            # Didn't remove any candidates
            return False
        self.candidates = new_candidates
        if len(self.candidates) == 1:
            self.set_value(new_candidates.pop())
        self.notify_all(TileEvent(self, EventKind.TileChanged))
        return True


# ------------------------------
#  Board class
# ------------------------------

class Board(object):
    """
    A board has a matrix of tiles
    """

    def __init__(self):
        """
        The empty board
        """

        self.groups = []
        self.tiles: List[List[Tile]] = []

        for row in range(NROWS):  # Create board with unknown values
            cols = []
            for col in range(NCOLS):
                cols.append(Tile(row, col))
            self.tiles.append(cols)

        for row in self.tiles:  # row groups
            self.groups.append(row)

        for col_i in range(len(self.tiles)):  # Making column groups
            col_group = []
            for row_i in range(len(self.tiles)):
                col_group.append(self.tiles[row_i][col_i])
            self.groups.append(col_group)

        for block_row in range(ROOT):  # Block groups
            for block_col in range(ROOT):
                group = []
                for row in range(ROOT):
                    for col in range(ROOT):
                        row_addr = (ROOT * block_row) + row
                        col_addr = (ROOT * block_col) + col
                        group.append(self.tiles[row_addr][col_addr])
                self.groups.append(group)

    def set_tiles(self, tile_values: Sequence[Sequence[str]]):
        """
        Set the tile values a list of lists or a list of strings
        """

        for row_num in range(NROWS):
            for col_num in range(NCOLS):
                tile = self.tiles[row_num][col_num]
                tile.set_value(tile_values[row_num][col_num])

    def __str__(self) -> str:
        """
        In Sadman Sudoku format
        """

        row_syms = []

        for row in self.tiles:
            values = [tile.value for tile in row]
            row_syms.append("".join(values))

        return "\n".join(row_syms)

    def is_consistent(self) -> bool:
        """
        Check to see if board is valid against Sudoku rules.
        I.E. No duplicate values in row, columns, groups
        """

        for group in self.groups:
            used_values = set()
            for value in group:
                if value.value in used_values and value.value != UNKNOWN:
                    return False
                used_values.add(value.value)

        return True

    def naked_single(self) -> bool:
        """
        Eliminate candidates and check for sole remaining possibilities.
        Return value True means we crossed off at least one candidate.
        Return value False means we made no progress
        """

        naked_single = False

        for group in self.groups:
            used_values = set()
            for tile in group:
                if tile.value != UNKNOWN:
                    used_values.add(tile.value)
            for tile in group:
                if tile.value == UNKNOWN:  # keep true even if return value is false
                    naked_single = tile.remove_candidates(used_values) or naked_single

        return naked_single

    def hidden_single(self) -> bool:
        """
        Using the hidden single technique, find the candidate for a tile
        """

        hidden_single = False

        for group in self.groups:
            leftovers = set(CHOICES)
            for tile in group:
                if tile.value in leftovers:
                    leftovers.remove(tile.value)
            for value in leftovers:
                places_to_put_value = []
                for tiles in group:
                    if tiles.could_be(value):
                        places_to_put_value.append(tiles)
                        new_tile_val = tiles
                if len(places_to_put_value) == 1:
                    new_tile_val.set_value(value)
                    hidden_single = True
                else:
                    """
                    Not sure if needed since the method provides the desired function.
                    But I'm scared to remove it
                    https://i.redd.it/6b7und8rs1v21.png
                    """
                    hidden_single = False
        return hidden_single

    def solve(self):
        progress = True
        while progress:
            progress = self.naked_single()
            self.hidden_single()
        return
