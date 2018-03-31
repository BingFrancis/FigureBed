from pyevolve import GSimpleGA
from pyevolve import G1DList
from pyevolve import Selectors
from pyevolve import Initializators, Mutators
from pyevolve import Consts
from run_params import run
import time
import numpy as np

std_list = [1.4334,188.367,101.5,-18.2504,232.985,60.4292,0.053212,-0.788851,
0.0448838,-47.5092,0.0196005,0.0572934,0.079777,-35.3143,145.647,
0.106148,0.588197,0.68312,1.67395,-0.0602758,-0.0178124,0.171754,
1.39151,0.848509,
-0.20205,-0.419414,-0.253834,0]


# Find negative values
def eval_func(ind):
    score = 1000.0
    # time.sleep(1)
    paramList = []

    for x in xrange(0, len(ind)):
        paramList.append(ind[x] * std_list[x])


    score += run(paramList, 2, '../paramfiles/optimizing.txt')

    file = open('./out2', 'a')
    newLines = []
    for i in range(len(paramList)):
        newLines.append(str(paramList[i]) + ',')
    newLines.append(str(score - 1000) + '\n')
    file.writelines(newLines)
    file.close()

    return score


# Genome instance
genome = G1DList.G1DList(27)
genome.setParams(rangemin=0.8, rangemax=1.2)

# genome = G1DBinaryString.G1DBinaryString(27)

# Change the initializator to Real values
genome.initializator.set(Initializators.G1DListInitializatorReal)

# Change the mutator to Gaussian Mutator
genome.mutator.set(Mutators.G1DListMutatorIntegerGaussian)

# The evaluator function (objective function)
genome.evaluator.set(eval_func)

# Genetic Algorithm Instance
ga = GSimpleGA.GSimpleGA(genome)
ga.minimax = Consts.minimaxType["maximize"]
ga.selector.set(Selectors.GRouletteWheel)
# ga.setPopulationSize()
ga.nGenerations = 1000

# Do the evolution
ga.evolve(10)

# Best individual
print ga.bestIndividual()
