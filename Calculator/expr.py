"""
Jacob Rammer
Calculator expr.py
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


class BinOP(Expr):
    """Abstract base class for binary operators +, *, /, -"""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""

        return f"({str(self.left)} {self.opsym} {str(self.right)})"

    def __repr__(self) -> str:
        return f"{self.opname}(IntConst({self.left}), {repr(self.right)})"

    def __eq__(self, other: "Expr") -> bool:
        return type(self) == type(other) and \
               self.left == other.left and \
               self.right == other.right

    def eval(self) -> "IntConst":
        """Each concrete subclass must define _apply(int, int)->int"""
        left_val = self.left.eval()
        right_val = self.right.eval()
        return IntConst(self._apply(left_val.value, right_val.value))


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


class Plus(BinOP):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)
        self.opsym = "+"
        self.opname = "Plus"

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        left_val = self.left.eval()
        right_val = self.right.eval()
        return IntConst(left_val.value + right_val.value)

    def _apply(self, left: int, right: int) -> int:
        return left + right


class Times(BinOP):
    """left * right"""

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)
        self.opsym = "*"
        self.opname = "Times"

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        left_val = self.left.eval()
        right_val = self.right.eval()
        return IntConst(left_val.value * right_val.value)

    def _apply(self, left: int, right: int) -> int:
        return left * right


class Div(BinOP):
    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)
        self.opsym = "/"
        self.opname = "Div"

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        left_val = self.left.eval()
        right_val = self.right.eval()
        return IntConst(left_val.value // right_val.value)

    def _apply(self, left: int, right: int) -> int:
        return left // right


class Minus(BinOP):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)
        self.opsym = "-"
        self.opname = "Minus"

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        left_val = self.left.eval()
        right_val = self.right.eval()
        return IntConst(left_val.value - right_val.value)

    def _apply(self, left: int, right: int) -> int:
        return left - right


class UnOp(Expr):

    def __init__(self, left: Expr):
        self.left = left

    def __str__(self) -> str:
        return f"{self.opsym}{self.left}"

    def __repr__(self):
        return f"{self.opname}{repr(self.left)}"

    def eval(self) -> "IntConst":
        left_val = self.left.eval()

        return IntConst(self._apply(left_val))


class Neg(UnOp):
    """Negative representation"""

    def __init__(self, left: Expr):
        super().__init__(left)
        self.opsym = "~"
        self.opname = "Neg"

    def eval(self) -> "IntConst":
        left_val = self.left.eval()
        return IntConst(-1 * left_val.value)

    def _apply(self, left: int):
        return -1 * left


class Abs(UnOp):
    """Absolute value"""

    def __init__(self, left: Expr):
        super().__init__(left)
        self.opsym = "@"
        self.opname = "Abs"

    def eval(self) -> "IntConst":
        left_val = self.left.eval()
        return IntConst(abs(left_val.value))

    def _apply(self, left: int):
        return abs(left)


ENV = dict()


def env_clear():
    """Clear all variables in calculator memory"""

    global ENV
    ENV = dict()


class UndefinedVariable(Exception):
    """Raised when expression tries to use a variable that
    is not in ENV
    """
    pass


class Var(Expr):

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Var({self.name})"

    def eval(self):
        global ENV
        if self.name in ENV:
            return ENV[self.name]
        else:
            raise UndefinedVariable(f"{self.name} has not been assigned a value")

    def assign(self, value: IntConst):
        val = ENV[self.name] = value
        return val


class Assign(Expr):
    """Assignment:  x = E represented as Assign(x, E)"""

    def __init__(self, left: Var, right: Expr):
        assert isinstance(left, Var)  # Can only assign to variables!
        self.left = left
        self.right = right

    def eval(self) -> IntConst:
        r_val = self.right.eval()
        self.left.assign(r_val)
        return r_val

    def __str__(self) -> str:
        return f"{self.left} = {self.right}"

    def __repr__(self):
        return f"Assign({self.left},{self.right}"
