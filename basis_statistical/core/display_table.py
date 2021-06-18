from tabulate import tabulate


def display_table(data):
    table = tabulate(data, headers=data.columns, tablefmt='psql')
    print(table)
