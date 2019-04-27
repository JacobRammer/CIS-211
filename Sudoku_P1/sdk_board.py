"""
Jacob Rammer
sdk_board.py for sudoku
"""

from sdk_config import CHOICES, UNKNOWN, ROOT
from sdk_config import NROWS, NCOLS
import logging
import enum

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

    # def __repr__(self) -> str:
    #     """
    #     Return the representation of a tile with row
    #     """


test_tile = Tile(1, 1)
print(test_tile)
