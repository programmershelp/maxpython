import matplotlib.pyplot as plot

x = ['A', 'B', 'C', 'D', 'E']
y = [30, 9, 52, 12, 24]
colors = ['red', 'green', 'blue', 'yellow', 'cyan']

plot.bar(x, y, color = colors, edgecolor = 'black')

plot.title('test results')
plot.xlabel('Grades')
plot.ylabel('Number of students')

plot.grid(color = 'red', alpha = 0.5, linestyle = '--', linewidth = 1)
plot.show()