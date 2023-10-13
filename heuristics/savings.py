import pandas as pd
import numpy as np
from collections import deque


def readData(filepath):
    df = pd.read_csv(
        filepath_or_buffer=filepath,
        header=None,
        skiprows=6,
        skip_blank_lines=True,
        delim_whitespace=True,
        usecols=[1, 2],
        names=("n", "x", "y"),
    )
    df.dropna(inplace=True)

    return df.to_numpy()


def computeDistanceMatrix(cities):
    N = cities.shape[0]

    dist = lambda i, j: np.sqrt(
        (cities[i, 0] - cities[j, 0]) ** 2 + (cities[i, 1] - cities[j, 1]) ** 2
    )

    distMatrix = np.zeros((N, N), dtype=int)

    for i in range(N):
        for j in range(i + 1, N):
            distMatrix[i, j] = dist(i, j)

    return distMatrix


def computeSavingsMatrix(distMatrix):
    N = distMatrix.shape[0]

    savingsMatrix = np.full((N - 1, N - 1), -np.inf)

    saving = lambda i, j: distMatrix[0, i] + distMatrix[0, j] - distMatrix[i, j]

    for i in range(1, N):
        for j in range(i + 1, N):
            savingsMatrix[i - 1, j - 1] = saving(i, j)

    return savingsMatrix


def computeSortedPairs(savingsMatrix):
    N = savingsMatrix.shape[0]
    sortedInd = np.unravel_index(
        np.argsort(savingsMatrix, axis=None), savingsMatrix.shape
    )
    sortedPairs = []
    numPairs = N * (N - 1) / 2
    for i in range(len(sortedInd[0]) - int(numPairs), len(sortedInd[0])):
        sortedPairs.append((sortedInd[0][i], sortedInd[1][i]))

    return sortedPairs


def computePathCost(path, distMatrix):
    cost = 0
    for i in range(len(path) - 1):
        if path[i + 1] > path[i]:
            cost += distMatrix[path[i], path[i + 1]]
        else:
            cost += distMatrix[path[i + 1], path[i]]
    return cost


def solveTSP(filepath):
    cities = readData(filepath)
    N = cities.shape[0]

    distMatrix = computeDistanceMatrix(cities)
    savingsMatrix = computeSavingsMatrix(distMatrix)
    sortedPairs = computeSortedPairs(savingsMatrix)

    path = deque()
    path.append(sortedPairs[-1][0] + 1)
    path.append(sortedPairs[-1][1] + 1)
    sortedPairs.pop()

    print(path)

    while len(path) < N - 1:
        for i in range(len(sortedPairs) - 1, 0, -1):
            left = path[0] - 1
            right = path[-1] - 1

            hasLeft = left in sortedPairs[i]
            hasRight = right in sortedPairs[i]

            if hasLeft and not hasRight:
                posLeft = sortedPairs[i].index(left)
                path.appendleft(sortedPairs[i][(posLeft + 1) % 2] + 1)
                for j in range(len(sortedPairs) - 1, 0, -1):
                    if left in sortedPairs[j]:
                        sortedPairs.pop(j)
                break

            elif hasRight and not hasLeft:
                posRight = sortedPairs[i].index(right)
                path.append(sortedPairs[i][(posRight + 1) % 2] + 1)
                for j in range(len(sortedPairs) - 1, 0, -1):
                    if right in sortedPairs[j]:
                        sortedPairs.pop(j)
                break

    print(path)
    print(len(path))
    for i in range(52):
        if path.count(i) > 1:
            print("ops:", i)

    path.appendleft(0)
    path.append(0)

    cost = computePathCost(path, distMatrix)
    print(cost)

    return path, cost
