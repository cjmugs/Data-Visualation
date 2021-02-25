import matplotlib.pyplot as plt

# Items to be plotted and line size
input_values = [7, 14, 21, 28, 35, 47, 59, 66, 73, 80]
squares = [1, 4, 9, 16, 25, 32, 45, 56, 68, 72]
cubes = [3, 9, 16, 23, 44, 56, 77, 87, 90, 99]
plt.plot(input_values, squares, linestyle="--", linewidth=5)
plt.plot(input_values, cubes, linewidth=5)


# Plot title and x,y labels
plt.title("Stuff People Should Know", fontsize=24)
plt.xlabel("Days of the year", fontsize=14)
plt.ylabel("Amount of Idiots", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

# Adds a grid to the background
plt.grid(b=True, linewidth=0.5)

# Calls the plotter
plt.show()