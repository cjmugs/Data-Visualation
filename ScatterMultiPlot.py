import matplotlib.pyplot as mp

# Values
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# This is what scatters the points
mp.scatter(x_values, y_values, s=100)

# Title and Labels
mp.title("Multi Scatter Plot", fontsize=20)
mp.xlabel("Value", fontsize=14)
mp.ylabel("Square of a Value", fontsize=14)

mp.show()