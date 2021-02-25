import matplotlib.pyplot as mp
from random_walk import RandomWalk
while True:
    # Make a random walk, and plot the points
    rw = RandomWalk(50000)
    rw.fill_walk()
    mp.figure(figsize=(8,5))
    point_numbers = list(range(rw.num_points))
    mp.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=mp.cm.Purples, edgecolor='none', s=1)
    
    # Emphasize the first and last points
    mp.scatter(0,0,c='green', edgecolors='none', s=100)
    mp.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    mp.axes().get_xaxis().set_visible(False)
    mp.axes().get_yaxis().set_visible(False)
    mp.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running =='n':
        break