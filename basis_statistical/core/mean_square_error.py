"""
Cài đặt đại lượng thống kê cơ bản: MSE
"""
import numpy as np

def MSE(A, B, ax):
    return np.square(np.subtract(A, B)).mean(axis=ax)