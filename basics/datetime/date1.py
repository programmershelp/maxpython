import datetime

print ('The Date Today is  :', datetime.datetime.today())

date_today = datetime.date.today()
print (date_today)
print ('This Year   :', date_today.year)
print ('This Month    :', date_today.month)
print ('Month Name:',date_today.strftime('%B'))
print ('This Week Day    :', date_today.day)
print ('Week Day Name:',date_today.strftime('%A'))