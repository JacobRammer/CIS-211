"""
Jacob Rammer

"""


class Expr(object):
    """Abstract base class of all expressions."""

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        raise NotImplementedError("Each concrete Expr class must define 'eval'")

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        raise NotImplementedError("Each concrete Expr class must define __str__")

    def __repr__(self) -> str:
        """Implementations of __repr__ should return a string that looks like
        the constructor, e.g., Plus(IntConst(5), IntConst(4))
        """
        raise NotImplementedError("Each concrete Expr class must define __repr__")

    def __eq__(self, other: "Expr") -> bool:
        raise NotImplementedError("__eq__ method not defined for class")


class IntConst(Expr):

    def __init__(self, other: int):
        self.value = other

    def eval(self) -> "IntConst":

        return self

    def __eq__(self, other: Expr):

        return isinstance(other, IntConst) and self.value == other.value

    def __str__(self) -> str:

        return f"{self.value}"

    def __repr__(self) -> str:

        return f"IntConst({str(self.value)})"


class Plus(Expr):

    def __init__(self, left: int, right: int):

        self.left = left
        self.right = right

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""

        return f"({str(self.left)} + {str(self.right)})"

    def __repr__(self) -> str:

        return f"Plus(IntConst({self.left}), {repr(self.right)})"

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        left_val = self.left.eval()
        right_val = self.right.eval()
        return IntConst(left_val.value + right_val.value)


class Times(Expr):
    """left * right"""

    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        left_val = self.left.eval()
        right_val = self.right.eval()
        return IntConst(left_val.value * right_val.value)

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        return f"({str(self.left)} * {str(self.right)})"

    def __repr__(self) -> str:
        """Implementations of __repr__ should return a string that looks like
        the constructor, e.g., Plus(IntConst(5), IntConst(4))
        """
        return f"Times({repr(self.left)}, {repr(self.right)})"

    def __eq__(self, other: "Expr") -> bool:
        return isinstance(other, Times) and \
            self.left == other.left and \
            self.right == other.right

