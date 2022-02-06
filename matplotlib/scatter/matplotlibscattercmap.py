import matplotlib.pyplot as plot
import numpy as np

x = np.array([5,7,8,7,2,9,7,9,4,9,12,9,6])
y = np.array([65,66,67,68,69,70,71,72,73,74,75,76,77])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plot.title('Golf Scores')
plot.xlabel('Players')
plot.ylabel('Score')
plot.scatter(x, y, c=colors, cmap='rainbow')
plot.show()