import numpy as np
from utils.functions import computePathCost
from utils.neighborhoods import opt2, opt3, varOpt4


def search(x, distMatrix, N=[opt2, opt3, varOpt4]):
    k = 0
    while k < len(N):
        y, yCost = N[k](x, distMatrix)
        if yCost < computePathCost(x, distMatrix):
            x = y
            k = 0
        else:
            k += 1
    return x, computePathCost(x, distMatrix)
