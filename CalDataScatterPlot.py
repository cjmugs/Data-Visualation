import matplotlib.pyplot as mp

# Values for Scatter Plot (AutoData)
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]


# This is what scatters the points (c=changes the color)
mp.scatter(x_values, y_values,c=y_values,cmap=mp.cm.Purples, edgecolors='none', s=40)

# Title and Labels
mp.title("Multi Scatter Plot", fontsize=20)
mp.xlabel("Value", fontsize=14)
mp.ylabel("Square of a Value", fontsize=14)

# Sets the range for each axis
mp.axis([0, 1100, 0, 1100000])

# Saves the file
mp.savefig('square_plot.png', bbox_inches='tight')

mp.show()