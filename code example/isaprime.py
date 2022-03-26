# A function for checking if  anumber is a prime number 
def CheckPrime(num):  
    # Checking that given number is greater than 1  
    if num > 1:  
        # Iterating over the given number with for loop  
        for j in range(2, int(num/2) + 1):  
            # If the given number is divisible or not  
            if (num % j) == 0:  
                print(num, "is not a prime number")  
                break  
        # it is a prime number  
        else:  
            print(num, "is a prime number")  
    # If the number is 1  
    else:  
        print(num, "is not a prime number")
        
# Get input from the user  
num = int(input("Enter an input number:"))

# Print the result  
CheckPrime(num)  