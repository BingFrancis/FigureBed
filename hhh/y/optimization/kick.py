from pyevolve import GSimpleGA
from pyevolve import G1DList
from pyevolve import Selectors
from pyevolve import Initializators, Mutators
from pyevolve import Consts
from run_params import run
import time
import numpy as np

std_list = [-16.155321891055568,-118.94574002268958,-49.0573368618613,
114.49734317000089,27.093511567801276,56.65895221759296,5.333153982193821,-7.881565931921614,
-3.103131585235596,-1.2098751103915228,5.000775182873085,-6.017267272068568,3.6943627753113,
-0.16411604294659987,-0.08084359577763695,6.483680425814427,3.7629696858600292,1.427020919469831]
# Find negative values

def eval_func(ind):
    score = 1000.0
    # time.sleep(1)
    paramList = []

    for x in xrange(0, len(ind)):
        paramList.append(std_list[x]*ind[x])

    score += run(paramList, 2, '../paramfiles/optimizing.txt')
    file = open('./out2', 'a')
    newLines = []
    for i in range(len(paramList)):
        newLines.append(str(paramList[i]) + ',')
    newLines.append(str(score-1000) + '\n')
    file.writelines(newLines)
    file.close()


    return score


# Genome instance
genome = G1DList.G1DList(18)
genome.setParams(rangemin=0.8, rangemax=1)

# genome = G1DBinaryString.G1DBinaryString(27)

# Change the initializator to Real values
genome.initializator.set(Initializators.G1DListInitializatorReal)

# Change the mutator to Gaussian Mutator
genome.mutator.set(Mutators.G1DListMutatorRealGaussian)

# The evaluator function (objective function)
genome.evaluator.set(eval_func)

# Genetic Algorithm Instance
ga = GSimpleGA.GSimpleGA(genome)
ga.minimax = Consts.minimaxType["maximize"]
ga.selector.set(Selectors.GRouletteWheel)
# ga.setPopulationSize()
ga.nGenerations = 100000000

# Do the evolution
ga.evolve(10)

# Best individual
print ga.bestIndividual()
