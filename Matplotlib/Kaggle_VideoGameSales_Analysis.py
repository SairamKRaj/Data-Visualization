import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Reading the input and creating the dataframe - 1 pt
dfVG = pd.read_csv('vgsales.csv')
pd.set_option('display.max_columns', None)

# Filtering the dataframe using the given conditions and printing the required total sales - 2 pts
'''
1 pt for filtering the required data from the dataframe
0.5 pts for computing the Total North America Sales
 0.5 pts for computing the Total Global Sales
'''
df = dfVG[(dfVG['Year'] >= 1980) & (dfVG['Year'] <= 2016)]
north_sales = np.sum(df.NA_Sales)
global_sales = np.sum(df.Global_Sales)
print(north_sales)
print(global_sales)

# Generating the required subplot - 0.5 pts
fig = plt.figure()
axes = fig.add_subplot(1,1,1)

# Plotting the required graphs along with labelling them - 3 pts (1.5 pts each). No label for any plot: 0.5 pts deducted
plt.plot(dfVG.groupby(['Year']).sum().loc[:, 'Global_Sales'], 'b.--', label='Global Sales')
plt.plot(dfVG.groupby(['Year']).sum().loc[:, 'NA_Sales'], 'g.--', label='NA Sales')

# Set x-axis and y-axis ticks - 1 pt (0.5 pts each)
x_ticks = np.arange(1980, 2016, 2)
y_ticks = np.arange(0, 701, 100)
axes.set_xticks(x_ticks)
axes.set_yticks(y_ticks)

# Plot grid in the graph - 0.5 pts
axes.grid(which='major')

# Assign x-axis and y-axis label - 1 pt (0.5 pts each)
plt.xlabel('Year')
plt.ylabel("Total Sales")

# Plot the legend of the graph - 0.5 pts
plt.legend(loc='upper left')

# Limit the tick values along x-axis and y-axis - 0.5 pts
plt.xlim(1980, 2015)
plt.ylim(0,700)
plt.show()