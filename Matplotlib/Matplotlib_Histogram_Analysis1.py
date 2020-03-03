import matplotlib.pyplot as plt
import numpy as np

# Generating normalized data (400 data points) randomly - 0.5 pt
randNum = np.random.randn(400)

# Plot the required graph with allocations for subplots - 1 pts
fig = plt.figure()
axes = fig.subplots(2, 2, sharex=True, sharey=True)

# Plot the normalized data with bins = 20 - 2 pts
axes[0, 0].hist(randNum, bins=20, color='m')
axes[0, 0].grid(which='major')

# Plot the normalized data with bins = 40 - 2 pts
axes[0, 1].hist(randNum, bins=40, color='m')
axes[0, 1].grid(which='major')

# Plot the normalized data with bins = 60 - 2 pts
axes[1, 0].hist(randNum, bins=60, color='m')
axes[1, 0].grid(which='major')

# Plot the normalized data with bins = 80 - 2 pts
axes[1, 1].hist(randNum, bins=80, color='m')
axes[1, 1].grid(which='major')

# Set x-axis ticks - 0.5 pts
plt.xticks([-3, -2, -1, 0, 1, 2])
plt.show()