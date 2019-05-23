"""
Jacob Rammer
In class two-pass example (this is preformed in linear time).
"""

from typing import List


# def label(fruits: List[str]) -> List[str]:
#     fruit_labels = []
#     counts = {}
#
#     for fruit in fruits:  # pass 1: count the fruit
#         if fruit in counts:
#             counts[fruit] += 1
#         else:
#             counts[fruit] = 1
#     so_far = {}
#     for fruit in fruits:  # pass 2: label the fruits
#         if fruit in so_far:
#             so_far[fruit] += 1
#         else:
#             so_far[fruit] = 1
#         fruit_labels.append(f"{fruit}, {so_far} of {counts[fruit]}")
#
#     return fruit_labels
#
#
# fruits = ["apple", "banana", "banana", "berry", "apple", "banana"]
# print(label(fruits))
#
# class Score(object):
#
#     def __init__(self, name: str, score: int):
#         self.name = name
#         self.score = score
#
#     def __repr__(self):
#         return f"Score({self.name}, {self.score})"
#
#
# def normalize(projects: List[Score]) -> List[Score]:
#     """
#     Returns the list of scores normalized as percent
#     of max score.
#     Pass 1: find the max score
#     Pass 2: build the normalized scores
#     """
#
#     if len(projects) == 0:
#         return []
#
#     max_score = 0
#     min_score = projects[0].score
#     for proj in projects:  # pass 1
#         max_score = max(max_score, proj.score)
#         min_score = min(min_score, proj.score)
#     result = []
#     max_range = max_score - min
#     for proj in projects:  # pass 2
#         score = int(((proj.score - min_score) / max_range) * 100)
#         normalized = Score(proj.name, score)
#         result.append(normalized)
#
#     return result
#
#
# scores = [Score("Leslie", 40), Score("Bobby", 23), Score("Adrian", 42)]
#
# print(normalize(scores))

def replace_missing_quizzes(quizzes: List[float]) -> None:
    """
    If no more than 3 quizzes are 0.0, replace them by the average
    of the remaining scores. Otherwise the list is not modified.
    Pass 1: average of non-zero scores and number of zero scores
    """

    sum_non_zero = 0
    count_nonzero = 0
    num_zero = 0
    for quiz in quizzes:  # pass 2
        if quiz == 0.0:
            num_zero += 1
        else:
            sum_non_zero += quiz
            count_nonzero += 1
    if count_nonzero == 0:
        average_non_zero = 0.0
    else:
        average_non_zero = sum_non_zero / count_nonzero

    if num_zero > 3:
        return None

    for i in range(len(quizzes)):
        if quizzes[i] == 0.0:
            quizzes[i] = average_non_zero

    return None


q = [0.0, 5.3, 20.4, 0.0, 8.3, 9.7]
# print(replace_missing_quizzes(q))
print(q)