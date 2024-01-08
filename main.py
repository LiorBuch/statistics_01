import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


def Empirical_F(vector):
    numpyArray = np.array(vector)
    uniArray = np.unique(vector)
    empiricalValues = [np.sum(numpyArray == i) / numpyArray.size for i in uniArray]
    for i in range(1, len(empiricalValues)):
        empiricalValues[i] = empiricalValues[i - 1] + empiricalValues[i]
    outputArray = np.column_stack((uniArray, empiricalValues))


