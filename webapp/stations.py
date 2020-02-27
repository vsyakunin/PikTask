import requests
import json

'''Функция отдает список всех станций метро в виде списка.'''

def hh_stations():
    stations_url = 'https://api.hh.ru/metro/1'
    stations=[]
    response = requests.get(stations_url)
    items = response.json()['lines']
    for line in items:
        for station in line['stations']:
            stations.append(station['name'])

    return stations
