import matplotlib.pyplot as plot

x = [30, 9, 52, 12, 24]
y = ['Apples', 'Pears', 'Oranges', 'Lemons', 'Limes']

plot.pie(x, labels = y)
plot.title("Fruit popularity",
     color = 'blue', fontweight = 'bold', fontsize = '16')
plot.show()