import matplotlib.pyplot as mp
mp.scatter(2, 4)

# This titles and labels the chart
mp.title("Scatter Chart", fontsize=20)
mp.xlabel("Value", fontsize=14)
mp.ylabel("Square of Value", fontsize=14)

# Size of the tick labels
mp.tick_params(axis='both', which='major', labelsize=14)

mp.show()