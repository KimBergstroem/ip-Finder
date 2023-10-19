################################################
######### Ip adress Locator for fun :D #########
################################################
#### pip install geocoder ######################
################################################
import geocoder as geo

# get your Own Ip Address
Ip_address = geo.ip('me')

# Find City of IP
Ip = geo.ip('192.xx.xxx.x')
Print(ip.city)

# Get latitude and longitude of IP Address
Print(ip.latlng)

# Get Area Info
Info = geo.google(‘City_name’)
Print(info.geojson)
Print(info.osm)
Print(info.wkt)
