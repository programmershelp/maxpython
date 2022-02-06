import matplotlib.pyplot as plot

x = ['A', 'B', 'C', 'D', 'E']
y = [30, 9, 52, 12, 24]
colors = ['red', 'green', 'blue', 'yellow', 'cyan']

plot.bar(x, y, color = colors, edgecolor = 'black',width = 0.50)

plot.title('test results', fontsize = '20')
plot.xlabel('Grades', fontsize = '14')
plot.xticks(color = 'black',rotation = 45, horizontalalignment = 'right')
plot.ylabel('Number of students', fontsize = '14')
plot.yticks(color = 'blue',rotation = 45, horizontalalignment = 'right')

plot.grid(color = 'red', alpha = 0.5, linestyle = '--', linewidth = 1)
plot.show()