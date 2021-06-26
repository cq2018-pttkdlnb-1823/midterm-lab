import numpy as np

def reject_outliers(data, alpha=2):
    return data[abs(data - np.mean(data)) < alpha * np.std(data)]
