from datetime import date
import holidays  
  
# Select country  
print (date(2022, 1, 1) in holidays.UK())
print (date(2022, 1, 24) in holidays.UK())
print (date(2022, 12, 25) in holidays.UK())