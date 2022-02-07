from geopy.geocoders import Nominatim  
geo_locator = Nominatim(user_agent = "geoapitest")

place_1 = "1964 Independence Ave SW"
location = geo_locator.geocode(place_1)  

print(location.address)
print(location.latitude, location.longitude)

data_1 = location.raw  
print (data_1)  
location_data = data_1['display_name'].split()  
print ("\nThe Full Location is: ")  
print (location_data)  
print ("The Zip code of the location is: ", location_data[-3])  