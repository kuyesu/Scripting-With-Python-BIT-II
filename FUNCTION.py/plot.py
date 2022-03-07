import random
import matplotlib.pyplot as plt

def plot_scatter(x, y, x_label, y_label, title):
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
    return None

def mainFunction():
    x = [random.randint(0, 100) for i in range(100)]
    y = [random.randint(0, 100) for i in range(100)]
    plot_scatter(x, y, 'X', 'Y', 'Scatter Plot')

mainFunction()