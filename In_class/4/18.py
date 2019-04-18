"""
Jacob Rammer

"""
from typing import List


class Family_Tree:

    def count(self) -> int:
        raise NotImplementedError("Hey, you forgot the count")


class Individual(Family_Tree):

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.text()

    def text(self, indent=0):
        return " " * indent * 3 + self.name

    def __repr__(self) -> str:
        return f"Individual(\"{self.name}\")"

    def count(self) -> int:
        return 1


class Family_Unit:
    """A composite unit, like an atomic family
    or extend family"""

    def __init__(self, parents: List[Individual], descendants: List[Family_Tree]):
        self.parents = parents
        self.descendants = descendants

    def __repr__(self) -> str:
        return f"Family_Unit({repr(self.parents)}, {repr(self.descendants)}"

    def __str__(self) -> str:
        return self.text()

    def count(self) -> int:
        total = len(self.parents)
        for d in self.descendants:
            total += d.count()

        return total

    def text(self, indent=0):
        result = ""
        sep = ""
        for parent in self.parents:
            result += sep + parent.text(indent)
        for descendant in self.descendants:
            result += "\n" + descendant.text(indent + 1)

        return result


toby = Individual("Sam")
marcie = Individual("Marcie")
ted = Individual("Ted")
print(repr(toby))

family = Family_Unit([ted], [toby, marcie])
print(family)

extended_family = Family_Unit([Individual("Zachariah")], [family, Individual("Jeb")])
print(extended_family)
print(f"The extend family of Zachariah has {extended_family.count()} persons")
