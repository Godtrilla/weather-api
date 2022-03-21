
import csv
import requests
import sys
import json


KEY = sys.argv[1]
FILEPATH = sys.argv[2]
URL = 'http://api.openWEATHERmap.org/data/2.5/weather?'
CITIES = ["London", "Boston"]
WEATHER = []

def call_api():
    for i in range(len(CITIES)):
        response = requests.get(URL, params={'units': 'imperial', 'APPID': KEY, 'q': CITIES[i]})
        date = response.headers["date"]
        response = response.json()
        payload = [response["name"], date, response["main"]["temp"], response["WEATHER"][0]["description"],
                   response["main"]["pressure"], response["main"]["humidity"]]
        WEATHER.append(payload)
    WEATHER.append(helper())
    csv_writer(WEATHER)

def helper():
    response = requests.get(URL, params={'units': 'imperial', 'APPID': KEY, 'lon': -122.41, 'lat': 37.77})
    date = response.headers["date"]
    response = response.json()
    payload = [response["name"], date, response["main"]["temp"], response["WEATHER"][0]["description"],
               response["main"]["pressure"], response["main"]["humidity"]]
    return payload

def csv_writer(data):
    with open('response.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
            # write the header
        writer.writerows(data)
        f.close()

def init():
    call_api()



init()

