# import modules
from datetime import datetime, timedelta

# get todays date
presentdate = datetime.now()
# work out yesterdays dat
yesterday = presentdate - timedelta(1)
#get tomorrows date
tomorrow = presentdate + timedelta(1)

# print the dates
print("Yesterday was :")
print(yesterday.strftime('%d-%m-%Y'))
print("Today is :")
print(presentdate.strftime('%d-%m-%Y'))
print("Tomorrow would be :")
print(tomorrow.strftime('%d-%m-%Y'))