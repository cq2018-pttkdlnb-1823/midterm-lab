import matplotlib.pyplot as plt 

def scatter_plot(first_attribute, second_attribute, title, x_label, y_label, cmap='viridis', figure_size=(12, 8), dpi=80):
    plt.figure(figsize=figure_size, dpi=dpi)
    plt.scatter(x=first_attribute, y=second_attribute)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()