"""
Cài đặt đại lượng thống kê cơ bản: Min
"""
import numpy as np


def minimum(data, axis):
    if type(data) is int or type(data) is float or type(data) is complex:
        return data
    else:
        return np.min(data, axis=axis)
