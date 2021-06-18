"""
Cài đặt đại lượng thống kê cơ bản: Hiệp phương sai
"""

import numpy as np
from basis_statistical.core.variance import variance


def covariance(data):
    return np.cov(np.array(data))

def cov(x, y):
    return np.matmul(x-np.mean(x), (y-np.mean(y)).T) / len(x)
