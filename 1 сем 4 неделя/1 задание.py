import numpy as np
import matplotlib.pyplot as plt

def one():
    fig = plt.figure(figsize = (10,7))
    ax1 = fig.add_subplot(111)

    x_measured = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_measured = [0, 10, 21, 32, 39, 48, 60, 70, 81, 92, 96]

    x = [0, 10]
    y = np.interp(x, x_measured, y_measured)

    ax1.scatter(x_measured, y_measured, marker='.')

    ax1.errorbar(x_measured, y_measured, yerr=3.5, xerr = 0.1, color = 'black', linestyle = 'None')

    ax1.plot(x,y, 'black')

    ax1.grid()

    ax1.set_title("График")
    ax1.set_xlabel("Время, с")
    ax1.set_ylabel("Напряжение, град.")

    plt.show()

