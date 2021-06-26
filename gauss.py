import numpy as np

def Gauss(mean, std):
    return np.random.normal(mean, std)

def Normalize(matrix):
    unit_zero = matrix - np.mean(matrix)
    standardization = unit_zero / np.std(unit_zero)
    return standardization
