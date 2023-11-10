import numpy as np


def computeDistanceMatrix(cities, distType="euclidean"):
    N = cities.shape[0]

    if distType == "euclidean":
        dist = lambda i, j: np.rint(
            np.sqrt(
                (cities[i, 0] - cities[j, 0]) ** 2 + (cities[i, 1] - cities[j, 1]) ** 2
            )
        )
    elif distType == "pseudo":
        dist = lambda i, j: np.ceil(
            np.sqrt(
                (
                    (cities[i, 0] - cities[j, 0]) ** 2
                    + (cities[i, 1] - cities[j, 1]) ** 2
                )
                / 10
            )
        )

    distMatrix = np.zeros((N, N), dtype=int)

    for i in range(N):
        for j in range(N):
            distMatrix[i, j] = dist(i, j)

    return distMatrix


def computePathCost(path, distMatrix):
    cost = 0
    for i in range(len(path) - 1):
        cost += distMatrix[path[i], path[i + 1]]
    cost += distMatrix[path[0], path[-1]]
    return cost
