"""
Hàm đọc dữ liệu
"""
import pandas as pd

def from_file_csv(file_path):
    pass

def wine_sample(file_path):
    data = pd.read_csv(file_path, header=None)
    data.columns = ["V"+str(i) for i in range(1, len(data.columns)+1)]  # rename column names to be similar to R naming convention
    return data