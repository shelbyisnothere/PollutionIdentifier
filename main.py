# Author: Shelby King
# Date: 7 January 2022
# Description: 
#   Simple python program to demonstrate how to pull information from an API.
import requests

import api_keys

def main():
    # Program title, seemed flashy
    print("---------------------- PollutionIdentifier ----------------------")
    # Two modes of input:
    #   Assess by City Name, or by Zipcode
    print("Please choose a form of location input:")
    print("\t[1] City Name")
    print("\t[2] Zipcode")
    mode = int(input("\nSelection: "))

    # Validate input
    if(mode < 0 or mode > 2):
        print("Error: Incorrect selection - please select option 1 or option 2.")
        return
    
    # Get JSON lattitude and longitude
    # TO DO: Improve input for city/zip-code by adding more validation and more specific input
    if(mode == 1):
        city = input("Please enter your city name: ")
        geocode_url = "http://api.openweathermap.org/geo/1.0/direct?q=" + city + "&appid=" + api_keys.open_weather_api_key
        req = requests.get(geocode_url)
        json = req.json()
        print(json)
        lattitude = str(json[0].get("lat"))
        longitude = str(json[0].get("lon"))
    else:
        zip = input("Please enter your zip-code: ")
        geocode_url = "http://api.openweathermap.org/geo/1.0/zip?zip=" + zip + "&appid=" + api_keys.open_weather_api_key
        req = requests.get(geocode_url)
        json = req.json()
        print(json)

    # Get pollution data
    # TO DO: Format pollution data output
    pollution_url = ("http://api.openweathermap.org/data/2.5/air_pollution?lat=" + lattitude
                        + "&lon=" + longitude 
                        + "&appid=" + api_keys.open_weather_api_key)
    req = requests.get(pollution_url)
    json = req.json()

    print("Pollution data for selected region: ")
    print(json)


    

main()