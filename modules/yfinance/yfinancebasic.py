# Import yfinance module  
import yfinance as yf  
# Using ticker for the Microsoft in yfinance function  
FBInfo = yf.Ticker("MSFT")  
# Looping over items to split them in key-value pair  
print("Items from the financial data of the Microsoft page in the key-value page: ")  
for keyItem, valueItem in FBInfo.info.items():  
    print(keyItem, ":", valueItem)  