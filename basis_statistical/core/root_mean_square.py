"""
Cài đặt đại lượng thống kê cơ bản: RMS
"""

from basis_statistical.core.mean_square_error import MSE

import numpy as np

def RMSE(A, B, axis):
    return np.sqrt(MSE(A, B, ax=axis))