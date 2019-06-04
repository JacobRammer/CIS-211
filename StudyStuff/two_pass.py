from typing import List

"""
Professor X gives several quizzes in a term. If a student misses a quiz, a
score of 0.0 is recorded. However, if a student misses up to three quizzes, those scores
will be replaced with the average of the other quiz scores. If a student misses more than
3 quizzes, none of the missing quiz scores will be replaced. Canvas doesn’t support this
grading method . . . help Professor X by writing a Python function to replace the missing
scores.
"""


def replace_missing_quizzes(quizzes: List[float]):
    num_of_zeros = 0
    total = 0

    for quiz in quizzes:
        if quiz == 0.0:
            num_of_zeros += 1
        total += quiz

    if num_of_zeros > 3:
        return
    else:
        average = total / (len(quizzes) - num_of_zeros)  # don't use 0 scores to calc. avg
        index = 0
        for quiz in quizzes:
            if quiz == 0.0:
                quizzes[index] = average
            index += 1


# scores = [15.0, 0.0, 3.0, 12.0]
# replace_missing_quizzes(scores)
# print(scores)

"""
Complete the select_cheeses function. This will probably require a two-pass
algorithm. Note the requirement to preserve order, which rules out sorting.
"""


class Cheese(object):

    def __init__(self, name: str, smelliness: str):
        self.name = name
        self.smelliness = smelliness

    def __repr__(self):
        return f"{self.name}, ({self.smelliness})"


def select_cheeses(cheese: List[Cheese]) -> List[Cheese]:
    """
    Returns a list of selected cheeses, which are those with
    smelliness strictly greater than the average smelliness
    of all the cheeses in the list. Cheeses in the returned list
    are in the same order as they appear in the input list.
    """

    total = 0
    cheese_list = []

    for rotten_milk in cheese:
        total += rotten_milk.smelliness

    average = total / len(cheese)

    for milk_curds in cheese:
        if milk_curds.smelliness > average:
            cheese_list.append(milk_curds)

    return cheese_list


# cheeses = [Cheese("brie", 5), Cheese("stilton", 2), Cheese("camembert", 6),
#            Cheese("provolone", 1), Cheese("parmigiano", 2)]
# print("Selected {}".format(select_cheeses(cheeses)))

"""
 Sometimes a project is really hard. For example, it might be worth 100
points, but maybe the highest score anyone earns is 42. In such a case I might want to use
a normalized score based on the highest actual score. For example, the student whose score
is 42 (the highest in the class) would receive a normalized score of 100, and a student who
earned 21 would get a normalized score of 50, because 21 is half of 42.
Finish the method “normalize” below to compute adjusted scores. You can round down to
an integer, or not, as you prefer.
"""


class Score(object):

    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"Score(\"{self.name}\", {self.score}"


def normalize(projects: List[Score]) -> List[Score]:
    high_score = 0
    normalized_scores = []

    if len(projects) == 0:
        return normalized_scores

    for project in projects:
        if project.score > high_score:
            high_score = project.score

    scale_factor = 100 / high_score

    for failure in projects:
        normalized_score = int(failure.score * scale_factor)
        normalized_scores.append(Score(failure.name, normalized_score))

    return normalized_scores


scores = [Score("Leslie", 40), Score("Bobby", 23), Score("Adrian", 42)]
print(normalize(scores))
