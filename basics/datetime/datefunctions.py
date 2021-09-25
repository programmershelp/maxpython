from datetime import datetime
 
dt = datetime.now()
print('Date and Time = ', dt)
 
print('Replace in Date = ', dt.replace(hour = 2))
print('Tzinfo from Date = ', dt.tzinfo)
print('Tzname from Date = ', dt.tzname())
 
print('Timetz from Date = ', dt.timetz())
print('Timestamp from Date = ', dt.timestamp())
print('Time from Date = ', dt.ctime())
print('isoweekday from Date = ', dt.isoweekday())
 
print('astimezone from Date = ', dt.astimezone())
print('utcoffset from Date = ', dt.utcoffset())
print('Daylight Saving from Date = ', dt.dst())