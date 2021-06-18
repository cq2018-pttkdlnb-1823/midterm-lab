"""
Cài đặt đại lượng thống kê cơ bản: Phương sai
"""
import numpy as np
from basis_statistical.core.mean import mean


def variance(data, sample=True):
    n = len(data)
    m = mean(data)
    deviations = [(x - mean) ** 2 for x in data]
    return sum(deviations) / n
