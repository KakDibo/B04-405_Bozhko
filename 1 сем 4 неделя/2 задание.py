import numpy as np 
import matplotlib.plot as plt
import pandas as pd
def two():

    fig = plt.figure(figsize = (10,7))
    ax1, ax2, ax3 = fig.subplots(1, 3)
    

    pos = 0
    scale = 10
    size = 500
    
    values = np.random.normal(pos, 10, size)
    
    ax1.hist(values, 100)
    

    pos = 0
    scale = 10
    size = 10000
    
    values = np.random.normal(pos, 10, size)
    
    ax2.hist(values, 100)

    pos = 0
    scale = 10
    size = 100000
    
    values = np.random.normal(pos, 10, size)
    
    ax3.hist(values, 100)

    plt.show()