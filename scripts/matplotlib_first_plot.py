# matplotlib_first_plot.py

# using pyplot functions

import matplotlib.pyplot as plt

# Data for plotting
time = [2, 4, 6, 8, 10]
distance = [1, 4, 9, 19, 39]
velocity = [1, 16, 26, 36, 111]

plt.figure(figsize=(9,7), dpi=100)

plt.plot(time,distance,'bo-', label='distance')
plt.plot(time,velocity, label='velocity')  # scaling, another y-axis???

plt.xlabel("Time")
plt.ylabel("Distance")

plt.legend()
plt.grid(True)