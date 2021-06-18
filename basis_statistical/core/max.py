"""
Cài đặt đại lượng thống kê cơ bản: Max
"""
import numpy as np


def maximum(data, axis):
    if type(data) is int or type(data) is float or type(data) is complex:
        return data
    else:
        return np.max(data, axis=axis)
