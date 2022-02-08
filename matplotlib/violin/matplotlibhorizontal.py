import matplotlib.pyplot as plot
import numpy as np

np.random.seed(1)

#creating dataset
data1 = np.random.normal(10, 10, 1000)
data2 = np.random.normal(50, 30, 1000)
data3 = np.random.normal(40, 20, 1000)
data4 = np.random.normal(0, 30, 1000)
data5 = np.random.normal(60, 10, 1000)
data = [data1, data2, data3, data4, data5]

fig, ax = plot.subplots()

#drawing violin plot
ax.violinplot(data, vert=False, showmedians=True)

plot.show()