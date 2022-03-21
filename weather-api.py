
import csv
import requests
import sys
import json

# GLOBALS ---->
# URL FOR API CALL
URL = 'http://api.openWEATHERmap.org/data/2.5/weather?'

# LIST OF CITIES
CITIES = ["London", "Boston"]

# LIST TO HOLD PAYLOADS
WEATHER = []

"""
FUNCTIION TO MAKE THE CALL TO THE OPENWEATHER API
"""
def call_api():
    for i in range(len(CITIES)):
        response = requests.get(URL, params={'units': 'imperial', 'APPID': KEY, 'q': CITIES[i]})
        date = response.headers["date"]
        response = response.json()
        payload = [response["name"], date, response["main"]["temp"], response["weather"][0]["description"],
                   response["main"]["pressure"], response["main"]["humidity"]]
        WEATHER.append(payload)
    WEATHER.append(helper())
    csv_writer(WEATHER)


"""
Helper function to gather data on San Francisco based on latitude and longitude
"""
def helper():
    response = requests.get(URL, params={'units': 'imperial', 'APPID': KEY, 'lon': -122.41, 'lat': 37.77})
    date = response.headers["date"]
    response = response.json()
    payload = [response["name"], date, response["main"]["temp"], response["weather"][0]["description"],
               response["main"]["pressure"], response["main"]["humidity"]]
    return payload

"""
Function that writes paylaod result to CSV
"""
def csv_writer(data):
        path = FILEPATH + "response.csv"
        with open(path, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
                # write the header
            writer.writerows(data)
            f.close()

"""
Initialization fucntion
"""
if __name__=="__main__":
    try:
        FILEPATH = sys.argv[2]
        KEY = sys.argv[1]
        call_api()
    except IndexError:
        print("You did not specify a file path")
        sys.exit(1)

