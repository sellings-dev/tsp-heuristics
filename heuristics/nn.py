import numpy as np
from utils.functions import computePathCost


def solveTSP(distMatrix):
    n = distMatrix.shape[0]
    path = [0]
    notInPath = list(range(1, n))
    for i in range(n - 1):
        min = 0
        for j in range(1, len(notInPath)):
            if distMatrix[path[i], notInPath[j]] < distMatrix[path[i], notInPath[min]]:
                min = j
        path.append(notInPath[min])
        notInPath.pop(min)

    return path, computePathCost(path, distMatrix)
