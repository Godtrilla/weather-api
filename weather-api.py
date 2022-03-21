
import csv
import requests
import sys
import json

key = sys.argv[1]
filepath = sys.argv[2]
url = 'http://api.openweathermap.org/data/2.5/weather?'
cities = ["London", "Boston"]
weather = []

def call_api():
    for i in range(len(cities)):
        response = requests.get(url, params={'units': 'imperial', 'APPID': key, 'q': cities[i]})
        date = response.headers["date"]
        response = response.json()
        payload = [response["name"], date, response["main"]["temp"], response["weather"][0]["description"],
                   response["main"]["pressure"], response["main"]["humidity"]]
        weather.append(payload)
    weather.append(helper())
    csv_writer(weather)

def helper():
    response = requests.get(url, params={'units': 'imperial', 'APPID': key, 'lon': -122.41, 'lat': 37.77})
    date = response.headers["date"]
    response = response.json()
    payload = [response["name"], date, response["main"]["temp"], response["weather"][0]["description"],
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

