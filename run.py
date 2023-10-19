################################################
######### Ip adress Locator for fun :D #########
################################################
#### pip install geocoder ######################
#### github.com/DenisCarriere/geocoder #########
################################################
import geocoder as geo

while True:

    # Input the IP address to look up
    ip_address = input("Enter an IP address: ")

    # Find the location of the IP address
    ip = geo.ip(ip_address)

    # Check if the location is found
    if ip.ok:
        city = ip.city
        country = ip.country
        postal = ip.postal
        org = ip.org
        latlng = ip.latlng
        location_name = ip.address

        print(f"IP Address: {ip_address}")
        print(f"Org.nr: {org}")
        print(f"City: {city}")
        print(f"Country: {country}")
        print(f"Post.nr: {postal}")
        print(f"Latitude and Longitude: {latlng}")
        print(f"Location Name: {location_name}")
    else:
        print(f"Location not found for IP address: {ip_address} , Please try again")

