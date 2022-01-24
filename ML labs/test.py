import pandas as pd
import numpy as np
import copy
from time import sleep
import sys
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.signal import argrelextrema
import seaborn as sns

series = np.array([1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 3, 3, 4, 3, 5, 7, 2, 3, 2, 4, 6, 9, 2, 3, 6, 8, 3, 54, 7, 3, 1])

sns.kdeplot(data=series)
density = sns.kdeplot(data=series)
mins = argrelextrema(series, np.less)
print(len(mins[0]), len(series[mins]))
sns.scatterplot(mins[0], series[mins])
print(mins)
print(series[mins])
plt.show()