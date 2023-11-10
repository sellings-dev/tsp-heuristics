import numpy as np
from utils.neighborhoods import randomKSwap
from utils.functions import computePathCost
from heuristics import vnd


def search(x, distMatrix, seed, kMax=2):
    rng = np.random.default_rng(seed)
    x, xCost = vnd.search(x, distMatrix)
    k = 0
    while k < kMax:
        x1 = randomKSwap(x, k + 2, rng)
        x2, x2Cost = vnd.search(x1, distMatrix)
        if x2Cost < xCost:
            x = x2
            xCost = x2Cost
            k = 0
        else:
            k += 1

    return x, xCost
