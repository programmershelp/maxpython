import matplotlib.pyplot as plot
import numpy as np

xlist = np.linspace(-5.0, 5.0, 100)
ylist = ylist = np.linspace(-5.0, 5.0, 100)
X, Y = np.meshgrid(xlist, ylist)

#creating hyperbolic plane
Z = (X**2)/4 - (Y**2)/9

fig, ax = plot.subplots()

#drawing filled contour plot
cb = ax.contourf(X, Y, Z)
#Adding a colorbar to the plot
fig.colorbar(cb) 

ax.set_title('Filled Contour Plot')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')

plot.show()