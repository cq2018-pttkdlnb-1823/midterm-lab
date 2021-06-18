"""
Cài đặt đại lượng thống kê cơ bản: Z-Scores
"""
import scipy.stats as stats

def z_scores(data):
    return stats.zscore(data)