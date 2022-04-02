# function to convert decimal to binary  
def dec_to_bin(myNumber):  
    decimal = int(myNumber)    
    # then, print the equivalent decimal
    print ("The given decimal number", decimal, "in Binary number is: ", bin(decimal))
    
# function to convert decimal to octal  
def dec_to_oct(myNumber):  
    decimal = int(myNumber)   
    # print the equivalent decimal  
    print ("The given decimal number", decimal, "in Octal number is: ", oct(decimal))
    
# function to convert decimal to hexadecimal  
def dec_to_hex(myNumber):  
    decimal = int(myNumber)     
    # print the equivalent decimal  
    print ("The given decimal number", decimal, " in Hexadecimal number is: ", hex(decimal))  
    
# test this all out 
myNumber = int (input (" Enter the Decimal Number: "))  
dec_to_bin(myNumber)  
dec_to_oct(myNumber)  
dec_to_hex(myNumber)  