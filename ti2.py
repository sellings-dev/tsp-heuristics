import os
import numpy as np
from heuristics import vns, nn
from utils import io
from utils.functions import computeDistanceMatrix
from timeit import default_timer as timer

optimal = {
    "att48": 10628,
    "berlin52": 7542,
    "kroA100": 21282,
    "kroA150": 26524,
    "kroA200": 29368,
    "kroB100": 22141,
    "kroB150": 16130,
    "kroB200": 29437,
    "kroC100": 20749,
    "kroD100": 21294,
    "kroE100": 22068,
    "lin105": 14379,
    "pr107": 44303,
    "pr124": 59030,
    "pr136": 96772,
    "pr144": 58537,
    "pr152": 73682,
    "pr76": 108159,
    "rat195": 2323,
    "rat99": 1211,
    "st70": 675,
}

row = "{: <15} | {: <15} | {: <20} | {: <20} | {: <20} | {: <20} | {: <25} | {: <25} "
print(
    row.format(
        "Instância",
        "Solução ótima",
        "Custo médio",
        "STD custo",
        "% acima do ótimo",
        "std % acima",
        "Tempo de execução médio",
        "STD tempo de execução",
    )
)

dataFolder = "./data/EUC_2D/"

for file in os.listdir(dataFolder):
    cities = io.readData(dataFolder + file)
    # cities = io.readData("./data/att48.tsp")
    distMatrix = computeDistanceMatrix(cities)

    costs = np.empty((2,))
    times = np.empty((2,))

    for i in range(2):
        start = timer()
        x1, x1Cost = nn.solveTSP(distMatrix)
        x2, x2Cost = vns.search(x1, distMatrix, i + 1)
        finish = timer()
        costs[i] = x2Cost
        times[i] = finish - start

    meanCost = np.mean(costs)
    stdDevCost = np.std(costs)
    meanExecTime = np.mean(times)
    stdDevExecTime = np.std(times)

    instance = file.split(".")[0]
    # instance = 'att48'

    print(
        row.format(
            instance,
            optimal[instance],
            meanCost,
            stdDevCost,
            (meanCost / optimal[instance] - 1) * 100,
            (stdDevCost / optimal[instance]) * 100,
            meanExecTime,
            stdDevExecTime,
        )
    )
