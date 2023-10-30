from heuristics import savings
from utils import io
import numpy as np
import os

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

row = "{: <15} | {: <15} | {: <20} | {: <20} | {: <20} | {: <20} | {: <25} | {: <25} | {: <25} | {: <25}"
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
        "Tempo total médio",
        "STD tempo total",
    )
)

dataFolder = "./data/EUC_2D/"

for file in os.listdir(dataFolder):
    cities = io.readData(dataFolder + file)
    # cities = io.readData("./data/att48.tsp")
    N = cities.shape[0]

    costs = np.empty((N,))
    execTimes = np.empty((N,))
    totalTimes = np.empty((N,))

    for i in range(N):
        path, costs[i], execTimes[i], totalTimes[i] = savings.solveTSP(
            cities, hub=i, benchmark=True
        )

    meanCost = np.mean(costs)
    stdDevCost = np.std(costs)
    meanExecTime = np.mean(execTimes)
    stdDevExecTime = np.std(execTimes)
    meanTotalTime = np.mean(totalTimes)
    stdDevTotalTime = np.std(totalTimes)

    instance = file.split(".")[0]

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
            meanTotalTime,
            stdDevTotalTime,
        )
    )
