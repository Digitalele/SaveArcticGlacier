import urllib, os

myloc = r"/Users/lele/Desktop/maps/python" #replace with your own location
key = "&key=" + "" # Api key, works fine without bot got banned after 100 request

def GetStreet(Add,SaveLoc):
  base = "https://maps.googleapis.com/maps/api/staticmap?maptype=satellite&center="
  MyUrl = base + Add + key
  fi = Add + ".jpg"
  urllib.urlretrieve(MyUrl, os.path.join(SaveLoc,fi))

# End of the google maps link with longitude, latitude, zoom and picture size 
Tests = ["69.014840,-26.941554&zoom=8&size=600x600",
         "69.514840,-26.941554&zoom=8&size=600x600",
         "70.014840,-26.941554&zoom=8&size=600x600",
         "70.514840,-26.941554&zoom=8&size=600x600",
         "71.014840,-26.941554&zoom=8&size=600x600",
         "71.514840,-26.941554&zoom=8&size=600x600",
         "72.014840,-26.941554&zoom=8&size=600x600"]

for i in Tests:
  GetStreet(Add=i,SaveLoc=myloc)


