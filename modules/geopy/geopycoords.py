from geopy.geocoders import Nominatim  
geo_locator = Nominatim(user_agent = "geoapitest")

location = geo_locator.reverse("38.88939505, -77.04030796874613")

print(location.address)