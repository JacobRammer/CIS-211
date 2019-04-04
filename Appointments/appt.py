"""
Jacob Rammer

Provides Appt and Agenda classes
"""
from datetime import datetime

if __name__ == "__main__":
    print("Running usage example")


class Appt:
    """
    Appointment has a start time, end time, and title
    Usage example:
        appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
        appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")
        if appt2 > appt1:
            print(f"appt1 '{appt1}' was over when appt2 '{appt2}'  started")
        elif appt1.overlaps(appt2):
            print("Oh no, a conflict in the schedule!")
            print(appt1.intersect(appt2))
    Should print:
        Oh no, a conflict in the schedule!
        2018-03-15 15:00 15:30 | Early afternoon nap and Coffee break
    """

    def __init__(self, start: datetime, finish: datetime, desc: str):
        """An appointment from start time to end time with a descriptions, desc.
        Start and finish should be the time of day.
        """
        assert finish > start, f"Period finish ({finish}) must be after start ({start}"
        self.start = start
        self.finish = finish
        self.desc = desc

    def __eq__(self, other: "Appt") -> bool:
        """Equality means same time period, ignoring description"""

        return self.start == other.start and self.finish == other.finish

    def __lt__(self, other: "Appt") -> bool:
        """Check to see if appointment occurs before"""

        return self.finish < other.finish

    def __gt__(self, other: "Appt") -> bool:
        """Check to see if appointment occurs after each other"""

        return self.start > other.start


class Agenda:
    """TODO"""
