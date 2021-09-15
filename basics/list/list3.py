#!/usr/bin/python

years = ['1985', '1988', '1999', '2005', '2009' ];
print (years)
#removes the '2005' item
years.remove('2005')
print (years)
#remove the first item
del years[0]
print (years)
#removes the last item
years.pop()
print (years)