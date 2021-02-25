import matplotlib.pyplot as mp

# Values for Scatter Plot (AutoData)
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

# Color map 
mp.scatter(x_values, y_values,c=y_values,cmap=mp.cm.Purples, edgecolors='none', s=40)

mp.show()