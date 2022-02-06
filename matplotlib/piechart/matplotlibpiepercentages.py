import matplotlib.pyplot as plot

x = [30, 9, 52, 12, 24]
y = ['Apples', 'Pears', 'Oranges', 'Lemons', 'Limes']
color_list = ['red', 'green', 'blue', 'yellow', 'cyan']

plot.pie(x, labels = y, colors = color_list, autopct = '%1.1f%%')
plot.title("Fruit popularity",
     color = 'blue', fontweight = 'bold', fontsize = '16')
plot.show()