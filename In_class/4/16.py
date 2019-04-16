"""
Jacob Rammer

"""


class Ingredient:
    def cost(self) -> float:
        raise NotImplementedError("Hey, you forgot the 'cost' method")


class Crust(Ingredient):

    def __init__(self, diam_in_cm: int):
        self.size = diam_in_cm

    def cost(self) -> float:
        area = (self.size / 2) * (self.size / 2) * 22 / 7
        return 0.42 * area


class Pizza(Ingredient):

    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def cost(self) -> float:
        total = 0
        for ingredient in self.ingredients:
            total += ingredient.cost()

        return total


class SimpleSauce(Ingredient):

    def __init__(self, crust: Crust):
        self.size = crust.size

    def cost(self) -> float:
        if self.size < 25:
            return 0.50
        else:
            return 1.00

my_pizza = Pizza()
the_crust = Crust(28)
my_pizza.add_ingredient(the_crust)
my_pizza.add_ingredient(SimpleSauce(the_crust))

print(f"my pizza costs {my_pizza.cost()}")