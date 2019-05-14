"""
Jacob Rammer
"""

g = lambda x, y: x + y
# print(g(3, 4))

ops = {"add": lambda x, y: x + y,
       "sub": lambda x, y: x - y,
       "mul": lambda x, y: x * y}


def apply(op, x, y):
    return ops[op](x, y)


# print(apply("add", 13, 7))


# Tree traversal

class FoodTree:

    def list_dangerous_ingredients(self, danger) -> list:
        raise NotImplementedError("Implement this method")


class Leaf(FoodTree):

    def __init__(self, name: str, potential_worries: list):
        self.name = name
        self.worries = potential_worries

    def list_dangerous_ingredients(self, danger) -> list:
        result = []
        if danger.oh_no(self):
            result.append(self.name)
        return result


class Inner(FoodTree):

    def __init__(self, name: str, ingredients: list):
        self.name = name
        self.ingredients = ingredients

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def list_dangerous_ingredients(self, danger) -> list:
        result = []
        for i in self.ingredients:
            result += i.list_dangerous_ingredients(danger)
        return result


class Danger:

    def oh_no(self, ingredient: Leaf) -> bool:
        raise NotImplementedError


class Vegan(Danger):

    def oh_no(self, ingredient: Leaf) -> bool:
        if "meat" in ingredient.worries:
            return True
        if "dairy" in ingredient.worries:
            return True
        return False


pizza = Inner("Pizza", [Inner("Sauce", [Leaf("tomato", ["stains"]), Leaf("anchovies", ["meat"])]),
                        Leaf("crust", ["gluten"]),
                        Leaf("sausage", ["meat"])])

print(pizza.list_dangerous_ingredients((Vegan())))
