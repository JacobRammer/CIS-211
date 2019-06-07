"""
Jacob Rammer

"""

from typing import List


class SummaryHook:
    """Abstract base class"""

    def __init__(self, initial: int = 0):
        self.summary = initial

    def get(self) -> int:
        return self.summary

    def visit(self, cell: int):
        raise NotImplementedError("Oops")


class Summarizable:
    def __init__(self, elements: List[int] = []):
        self.elements = elements

    def foreach(self, hook: SummaryHook) -> int:
        for cell in self.elements:
            hook.visit(cell)
        return hook.get()


class Sm(SummaryHook):

    def visit(self, cell: int):
        self.summary += cell


class Mx(SummaryHook):
    def visit(self, cell: int):
        t = self.summary
        if cell > self.summary:
            self.summary = cell


s = Summarizable([10, 30, 20])
# summary = s.foreach(Sm())
# print(f"Summarized by Sm to {summary}")
summary = s.foreach(Mx())
print(f"Summarized by Mx to {summary}")
