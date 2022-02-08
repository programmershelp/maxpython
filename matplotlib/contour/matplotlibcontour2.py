import numpy as np
import matplotlib.pyplot as plot

xlist = np.linspace(-2.0, 2.0, 100)
ylist = np.linspace(-2.0, 2.0, 100)
X, Y = np.meshgrid(xlist, ylist)
Z = np.sqrt(X**2 + Y**2)

plot.figure()

contour = plot.contour(X, Y, Z)
plot.clabel(contour, colors = 'k', fmt = '%2.1f', fontsize=10)
c = ('red', 'yellow', 'blue', '0.4', 'c', 'm')
contour_filled = plot.contourf(X, Y, Z, colors=c)
plot.colorbar(contour_filled)

plot.title('Filled Contours Plot')
plot.xlabel('x (cm)')
plot.ylabel('y (cm)')
plot.show()