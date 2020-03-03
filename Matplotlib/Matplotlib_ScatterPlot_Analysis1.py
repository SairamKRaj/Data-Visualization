import matplotlib.pyplot as plt
import numpy as np

# Generate the required data points - 2 points
x = np.random.randint(0, 200, 100)
y = np.random.randint(0, 300, 100)

# Plot the graph for both the data points with correct color format - 1 pt
plt.plot(x, 'g.')
plt.plot(y, 'g.')

# Set y-axis and x-axis ticks - 2 pts
plt.yticks([0, 50, 100, 150, 200, 250, 300])
plt.xticks([0, 50, 100, 150, 200, 250, 300])

# Set title for the plot with green color - 2 pt (1 pt for each task)
title_obj = plt.title('Scatter plot of random integers')
plt.setp(title_obj, color='g')

# Plot the x-axis label - 1 pt
plt.xlabel('Random integers 1 to 200')

# Plot the y-axis label - 1 pt
plt.ylabel('Random integers 1 to 300')

# Plotting grid in the graph - 1 pt
plt.grid(which='major')

plt.show()