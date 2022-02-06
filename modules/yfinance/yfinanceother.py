# Import yfinance module  
import yfinance as yf  
# Using ticker for the Microsoft in yfinance function  
msInfo = yf.Ticker("MSFT")  
# Microsoft financial data we retrieved  
sectorInfo = msInfo.info['sector'] # Company Sector key  
shortNameInfo = msInfo.info['shortName'] # Price Earning ratio key  
weekInfo = msInfo.info['52WeekChange'] # Company Beta key  
# Print the Company Sector Information  
print("Sector is: ", sectorInfo)  
# Print the Short name  
print("The Short name is ", shortNameInfo)  
# Print the 52 week info
print("52 week info: ", weekInfo)  