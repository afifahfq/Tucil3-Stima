from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):

      #R = 3959.87433 # this is in miles.  For Earth radius in kilometers use 6372.8 km
      R = 6372.8 * 1000

      dLat = radians(lat2 - lat1)
      dLon = radians(lon2 - lon1)
      lat1 = radians(lat1)
      lat2 = radians(lat2)

      a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
      c = 2*asin(sqrt(a))

      return R * c

# Usage
lon1 = -6.893683111882957
lat1 = 107.60843476284668
lon2 = -6.893208410946931
lat2 = 107.6104105457172

print(haversine(lat1, lon1, lat2, lon2))