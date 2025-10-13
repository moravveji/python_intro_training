# matplotlib_first_plot_oo.py

# using oo approach

import matplotlib.pyplot as plt

# Data for plotting
time = [2, 4, 6, 8, 10]
distance = [1, 4, 9, 19, 39]
velocity = [1, 16, 26, 36, 111]

fig, ax1 = plt.subplots()

ax1.set_ylabel("distance (m)")
ax1.set_xlabel("time")
ax1.plot(time, distance, "blue")

ax2 = ax1.twinx() # create another y-axis sharing a common x-axis


ax2.set_ylabel("velocity (m/s)")
ax2.set_xlabel("time")
ax2.plot(time, velocity, "green")

fig.set_size_inches(7,5)
fig.set_dpi(100)

plt.show()