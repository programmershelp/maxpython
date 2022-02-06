import matplotlib.pyplot as plot
import numpy as np

x = np.random.randint(50, size=(50))
y = np.random.randint(50, size=(50))
colors = np.random.randint(50, size=(50))
sizes = 10 * np.random.randint(50, size=(50))

plot.title('Scatter chart example')
plot.xlabel('X Axis')
plot.ylabel('Y Axis')

plot.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='rainbow')

plot.colorbar()

plot.show() 