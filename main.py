from basis_statistical.core.io import wine_sample
from basis_statistical.core.display_table import display_table

data = wine_sample('./data/wine/wine.data')

print(data.describe())