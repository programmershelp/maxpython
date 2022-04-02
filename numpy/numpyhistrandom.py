import matplotlib.pyplot as plot
import numpy as np

x = np.random.normal(75, 10, 250)
print(x)
plot.hist(x)
plot.show() 