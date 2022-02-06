import matplotlib.pyplot as plot

x = ['A', 'B', 'C', 'D', 'E']
y = [30, 9, 52, 12, 24]

plot.barh(x, y)

plot.title('test results')
plot.xlabel('Number of students')
plot.ylabel('Grades')

plot.grid(color = 'red', alpha = 0.5, linestyle = '--', linewidth = 1)
plot.show()