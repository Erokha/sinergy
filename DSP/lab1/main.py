import numpy as np
from copy import deepcopy

def normalize_max_crit(matrix: np.array, crit_num: int) -> np.array:
    m = deepcopy(matrix).transpose()
    mini = min(m[crit_num])
    div = max(m[crit_num]) - min(m[crit_num])
    m[crit_num] = [(i - mini) / div for i in m[crit_num]]
    return m.transpose()


def normalize_min_crit(matrix: np.array, crit_num: int) -> np.array:
    m = deepcopy(matrix).transpose()
    maxi = max(m[crit_num])
    div = max(m[crit_num]) - min(m[crit_num])
    m[crit_num] = [(maxi - i) / div for i in m[crit_num]]
    return m.transpose()


length = 4
matrix = np.array(
    [
        [3, 7, 2, 9],
        [8, 3, 6, 7],
        [4, 8, 3, 5],
        [9, 6, 5, 4]
    ]
).astype(float)
weight = np.array([8, 9, 6, 7])

matrix = normalize_max_crit(normalize_max_crit(normalize_max_crit(normalize_min_crit(matrix, 0), 1), 2), 3)
result = [sum(row * weight) for row in matrix]

print(result)
