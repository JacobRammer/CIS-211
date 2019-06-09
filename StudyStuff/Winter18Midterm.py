class Spillage(Exception):
    pass

class Bucket(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.holding = 0

    def pour_in(self, amount: int):
        space = self.capacity - self.holding
        if amount > space:
            raise Spillage("Too much! Overflowing")
        self.holding += amount

    def pour_out(self, req_amount):
        # pour_amount = min(self.holding, req_amount)
        # self.holding -= pour_amount
        # return 
        t = self.holding
        if req_amount > self.holding:
            self.holding = 0
            return t
        else:
            self.holding -= req_amount
            return req_amount


            
    
    def __str__(self):
        return f"holding {self.holding}"

# b = Bucket(20)
# b.pour_in(10)
# out = b.pour_out(7)
# assert out == 7
# out = b.pour_out(7)
# assert out == 3
# out = b.pour_out(3)
# assert out == 0


"""
Question # 6
"""


class Point(object):
    """Point.x and Point.y are 'public' fields"""

    def __init__(self, x, y): 
        self.listeners = []
        self.x = x
        self.y = y

    def add_listener(self, listener: "PointListener") -> None: 
        self.listeners.append(listener)

    def notify_all(self):
        for listener in self.listeners:
            listener.notify(self)

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy 
        self.notify_all()


class PointLinstener:

    def notify(self, other: Point):
        """
        This is the method to write.
        """

        print(f"Point moved to {other.x}, {other.y}")


# p = Point(5, 5)
# p.add_listener(PointLinstener())
# p.move(4, 3)
# p.move(3, 2)


"""
Question 8
"""

"""
The max_leafmethod for the Tree structure below should return 
the maxi-mum of leaf values. Complete the method. Be brief. 
(It may help to remember that thebuilt-in function max(m,n) 
returns the maximum of its arguments.)
"""

class Tree(object):
    """
    Abstract base class
    """

    def max_leaf(self):
        raise NotImplemented("Forgot to implement max_leaf")



class Leaf(Tree):

    def __init__(self, value: int):
        assert value > 0
        self.val = value

    def max_leaf(self) -> int:
        """
        This is the method to write.
        """

        return self.val  # base recursive case


class Interior(Tree):
    """
    Interior node has two subtrees
    """

    def __init__(self, left: Tree, right: Tree):
        self.left = left
        self.right = right

    def max_leaf(self) -> int:
        """
        This is the method to write
        """
        
        return max(self.left.max_leaf(), self.right.max_leaf())


t = Interior(Leaf(4),Interior(Leaf(5),Leaf(3)))
print(t.max_leaf())  # should be 5



