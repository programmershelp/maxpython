import matplotlib.pyplot as plot
import numpy as np

x = np.array([5,7,8,7,2,9,7,9,4,9,12,9,6])
y = np.array([65,66,67,68,69,70,71,72,73,74,75,76,77])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plot.title('Golf Scores')
plot.xlabel('Players')
plot.ylabel('Score')
plot.scatter(x, y, c=colors)
plot.show()