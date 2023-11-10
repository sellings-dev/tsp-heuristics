import numpy as np
from timeit import default_timer as timer
from collections import deque
from utils.functions import computeDistanceMatrix, computePathCost


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


def solveTSP(cities, distType="euclidean", hub=None, benchmark=False):
    N = cities.shape[0]

    if hub is not None:
        aux = np.copy(cities[hub])
        cities[hub] = np.copy(cities[0])
        cities[0] = np.copy(aux)

    if benchmark:
        startTime = timer()

    distMatrix = computeDistanceMatrix(cities, distType)
    savingsMatrix = computeSavingsMatrix(distMatrix)
    sortedPairs = computeSortedPairs(savingsMatrix)

    if benchmark:
        overheadTime = timer()

    path = deque()
    path.append(sortedPairs[-1][0] + 1)
    path.append(sortedPairs[-1][1] + 1)
    sortedPairs.pop()

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

    for i in range(52):
        if path.count(i) > 1:
            print("ops:", i)
            
    path.append(0)

    if benchmark:
        endTime = timer()

    cost = computePathCost(path, distMatrix)

    if benchmark:
        execTime = endTime - overheadTime
        totalTime = endTime - startTime
        return path, cost, execTime, totalTime

    return path, cost
