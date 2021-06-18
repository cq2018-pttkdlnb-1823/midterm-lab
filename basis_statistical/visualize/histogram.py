import matplotlib.pyplot as plt 

def histogram(data, xlabel, ylabel, bins=None, binwidth=None,  ec='black', figure_size=(12, 8), density=True):
    plt.figure(figsize=figure_size)
    if bins == None and binwidth != None:
        plt.hist(data, density=density, bins=range(int(min(data)), int(max(data)) + binwidth, binwidth), ec=ec)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
    if bins != None: 
        plt.hist(data, density=density, bins=bins, ec=ec)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()