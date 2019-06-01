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
        pour_amount = min(self.holding, req_amount)
        self.holding -= pour_amount
        return pour_amount
    
    def __str__(self):
        return f"holding {self.holding}"

b = Bucket(20)
b.pour_in(10)
out = b.pour_out(7)
assert out == 7
out = b.pour_out(7)
assert out == 3
out = b.pour_out(3)
assert out == 0
