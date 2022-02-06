import matplotlib.pyplot as plot
import numpy as np

x = np.array([5,7,8,7,2,9,7,9,4,9,12,9,6])
y = np.array([65,66,67,68,69,70,71,72,73,74,75,76,77])
sizes = np.array([90,500,100,200,50,70,60,20,10,300,600,800,1000])

plot.title('Golf Scores')
plot.xlabel('Players')
plot.ylabel('Score')
plot.scatter(x, y, s=sizes)
plot.show()