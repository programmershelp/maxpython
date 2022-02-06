import matplotlib.pyplot as plot
import numpy as np

x = np.array([5,7,8,7,2,9,7,9,4,9,12,9,6])
y = np.array([65,66,67,68,69,70,71,72,73,74,75,76,77])
plot.scatter(x, y)

x = np.array([4,2,8,6,7,9,8,6,5,9,8,11,10])
y = np.array([65,66,67,68,69,70,71,72,73,74,75,76,77])
plot.scatter(x, y)

plot.title('Golf Scores')
plot.xlabel('Players')
plot.ylabel('Score')

plot.show()
