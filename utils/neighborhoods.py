from utils.functions import computePathCost


def opt2(x, distMatrix):
    edgesCount = len(x) - 1
    for i in range(edgesCount - 2):
        for j in range(i + 2, edgesCount):
            costChange = (
                distMatrix[x[i], x[j]]
                + distMatrix[x[i + 1], x[j + 1]]
                - distMatrix[x[i], x[i + 1]]
                - distMatrix[x[j], x[j + 1]]
            )
            if costChange < 0:
                y = x[: i + 1] + list(reversed(x[i + 1 : j + 1])) + x[j + 1 :]
                return y, computePathCost(y, distMatrix)
    return x, computePathCost(x, distMatrix)


def opt3(x, distMatrix):
    edgesCount = len(x) - 1
    for i in range(edgesCount - 4):
        for j in range(i + 2, edgesCount - 2):
            for k in range(j + 2, edgesCount):
                removedCost = (
                    distMatrix[x[i], x[i + 1]]
                    + distMatrix[x[j], x[j + 1]]
                    + distMatrix[x[k], x[k + 1]]
                )
                addedCost1 = (
                    distMatrix[x[i], x[j]]
                    + distMatrix[x[i + 1], x[k]]
                    + distMatrix[x[j + 1], x[k + 1]]
                )
                if addedCost1 - removedCost < 0:
                    y = (
                        x[: i + 1]
                        + list(reversed(x[i + 1 : j + 1]))
                        + list(reversed(x[j + 1 : k + 1]))
                        + x[k + 1 :]
                    )
                    return y, computePathCost(y, distMatrix)

                addedCost2 = (
                    distMatrix[x[i], x[j + 1]]
                    + distMatrix[x[j], x[k]]
                    + distMatrix[x[k + 1], x[i + 1]]
                )
                if addedCost2 - removedCost < 0:
                    y = (
                        x[: i + 1]
                        + x[j + 1 : k + 1]
                        + list(reversed(x[i + 1 : j + 1]))
                        + x[k + 1 :]
                    )
                    return y, computePathCost(y, distMatrix)

                addedCost3 = (
                    distMatrix[x[i], x[k]]
                    + distMatrix[x[i + 1], x[j + 1]]
                    + distMatrix[x[j], x[k + 1]]
                )
                if addedCost3 - removedCost < 0:
                    y = (
                        x[: i + 1]
                        + list(reversed(x[j + 1 : k + 1]))
                        + x[i + 1 : j + 1]
                        + x[k + 1 :]
                    )
                    return y, computePathCost(y, distMatrix)

                addedCost4 = (
                    distMatrix[x[i], x[j + 1]]
                    + distMatrix[x[j], x[k + 1]]
                    + distMatrix[x[k], x[i + 1]]
                )
                if addedCost4 - removedCost < 0:
                    y = x[: i + 1] + x[j + 1 : k + 1] + x[i + 1 : j + 1] + x[k + 1 :]
                    return y, computePathCost(y, distMatrix)
    return x, computePathCost(x, distMatrix)


def varOpt4(x, distMatrix):
    edgesCount = len(x) - 1
    for i in range(edgesCount - 6):
        for j in range(i + 2, edgesCount - 4):
            for k in range(j + 2, edgesCount - 2):
                for l in range(k + 2, edgesCount):
                    removedCost = (
                        distMatrix[x[i], x[i + 1]]
                        + distMatrix[x[j], x[j + 1]]
                        + distMatrix[x[k], x[k + 1]]
                        + distMatrix[x[l], x[l + 1]]
                    )
                    addedCost = (
                        distMatrix[x[i], x[k + 1]]
                        + distMatrix[x[l], x[j + 1]]
                        + distMatrix[x[k], x[i + 1]]
                        + distMatrix[x[j], x[l + 1]]
                    )
                    if addedCost - removedCost < 0:
                        y = (
                            x[: i + 1]
                            + x[k + 1 : l + 1]
                            + x[j + 1 : k + 1]
                            + x[i + 1 : j + 1]
                            + x[l + 1 :]
                        )
                        return y, computePathCost(y, distMatrix)
    return x, computePathCost(x, distMatrix)


def randomKSwap(x, k, rng):
    n = len(x)
    swapIndexes = rng.integers(0, n, k)
    y = x.copy()
    for i in range(k - 1):
        y[swapIndexes[i]] = x[swapIndexes[i + 1]]
    y[swapIndexes[-1]] = x[swapIndexes[0]]
    return y
