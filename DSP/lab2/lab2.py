import numpy as np


def get_eigenvectors_array(matrix: np.array) -> np.array:
    return np.array([row.prod() ** (1 / len(row)) for row in matrix])


def get_eigenvectors_weight(eigenvectors: np.array) -> np.array:
    return np.array([item / eigenvectors.sum() for item in eigenvectors])


option_names = ['a', 'b', 'c', 'd']
k1 = np.array([
    [1, 1 / 5, 3, 1 / 2],
    [5, 1, 1 / 3, 1 / 7],
    [1 / 3, 3, 1, 3],
    [2, 7, 1 / 3, 1],
])
k2 = np.array([
    [1, 4, 3, 1 / 5],
    [1 / 4, 1, 2, 5],
    [1 / 3, 1 / 2, 1, 3],
    [5, 1 / 5, 1 / 3, 1],
])
k3 = np.array([
    [1, 3, 1 / 7, 5],
    [1 / 3, 1, 6, 3],
    [7, 1 / 6, 1, 1 / 5],
    [1 / 5, 1 / 3, 5, 1],
])
weight = np.array([
    [1, 3, 1 / 2],
    [1 / 3, 1, 5],
    [2, 1 / 5, 1],
])

crit_weights = [get_eigenvectors_weight(get_eigenvectors_array(x)) for x in [k1, k2, k3]]
weight_weight = get_eigenvectors_weight(get_eigenvectors_array(weight))

for i in range(len(option_names)):
    res = sum([crit_weights[j][i] * weight_weight[j] for j in range(len(crit_weights))])
    print(f"F({option_names[i]}) = {res}")
