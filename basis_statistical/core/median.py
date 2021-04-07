"""
Cài đặt đại lượng thống kê cơ bản: Median
"""
import numpy as np 

def median(data):
    if type(data) is int:
        return(float(data))
    elif type(data) is list:
        data.sort()

        if len(data) == 1:
            return(float(data[0]))
        elif len(data) % 2 == 1:
            return(float(data[int(len(data) / 2)]))

        middle_index = len(data) / 2
        return((data[int(middle_index - .5)] + data[int(middle_index + .5)]) / 2)
    else:
        return np.median(data)