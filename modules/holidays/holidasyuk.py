from datetime import date  
import holidays

# Select country  
uk_holidays_list = holidays.UnitedKingdom()

# printing all the holiday of India year 2022  
for p in holidays.UnitedKingdom(years = 2022).items():  
    print(p)  
