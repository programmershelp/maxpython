import numpy as np
import matplotlib.pyplot as plot

xlist = np.linspace(-3.0, 3.0, 100)
ylist = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(xlist, ylist)

Z = np.sqrt(X ** 2 + Y ** 2 )
plot.figure()

levels = [0.0, 0.2, 0.5, 0.9, 1.5, 2.5, 3.5]
contour = plot.contour(X, Y, Z, levels, colors='k')
plot.clabel(contour, colors = 'k', fmt = '%2.1f', fontsize=10)
contour_filled = plot.contourf(X, Y, Z, levels)
plot.colorbar(contour_filled)

plot.title('Plot from level list')
plot.xlabel('x (cm)')
plot.ylabel('y (cm)')
plot.show()