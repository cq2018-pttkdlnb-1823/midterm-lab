from basis_statistical.core.io import from_file_csv
from basis_statistical.core.display_table import display_table
from basis_statistical.core.mean import mean
from basis_statistical.core.min import minimum

data = from_file_csv('./data/wine/wine.data')

display_table(data=data)

print(mean(data))

print(minimum(data, axis=0))