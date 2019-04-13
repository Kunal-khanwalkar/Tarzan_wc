#Delaunay Triangulation

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    points = np.genfromtxt('plotdata.txt', delimiter=',')
    tri = Delaunay(points)
    ax1.clear()
    ax1.triplot(points[:,0],points[:,1],tri.simplices.copy())
    ax1.plot(points[:,0],points[:,1],'o')
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()