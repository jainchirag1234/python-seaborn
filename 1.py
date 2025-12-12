import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Load the 'diamonds' dataset
database = sb.load_dataset('diamonds')
print(database)

# Plot the distribution of 'carat' values
sb.histplot(database['carat'])
plt.show()

