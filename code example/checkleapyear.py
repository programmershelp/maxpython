# Default function to implement conditions to check leap year  
def CheckLeapYear(Year):  
  # Check the year is leap year  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("The Year is a leap Year");  
  # it is not a leap year  
  else:  
    print ("The Year is not a leap Year")  

# Get the year from user  
Year = int(input("Enter the year to check: "))

# Print result  
CheckLeapYear(Year)  