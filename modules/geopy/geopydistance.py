from geopy.distance import geodesic

newyork_ny = (40.7127281, -74.0060152)
sanfrancisco_ca = (37.15587905455899, -122.20509662089846)

print(geodesic(newyork_ny, sanfrancisco_ca).miles)