from datetime import datetime

startdate = datetime(2018, 6, 2)
enddate = datetime(2022, 4, 9)

diff = (enddate.year - startdate.year) * 12 + (enddate.month  - startdate.month )
print('Difference between dates in months: ')
print(diff)