from datetime import datetime
from dateutil import relativedelta

startdate = '2/6/2018'
enddate = '9/4/2022'

start = datetime.strptime(startdate, "%d/%m/%Y")
end =   datetime.strptime(enddate, "%d/%m/%Y")

# Get the interval between two dates
diffdate = relativedelta.relativedelta(end, start)
diffinmonths = diffdate.months + diffdate.years * 12

print('Difference between dates in months: ')
print(diffinmonths)