from flask import abort
import requests
import json

def hh_stations():
    """Функция отдает список всех станций метро в виде списка."""
    stations_url = 'https://api.hh.ru/metro/1'
    stations = []
    try:
        response = requests.get(stations_url)
        items = response.json()['lines']
        for line in items:
            for station in line['stations']:
                stations.append(station['name'])
        return stations
    
    except KeyError:
        print('Requested URL is not availiable')
        abort(404)
    except requests.exceptions.HTTPError:
        print ('HTTP Error')
        abort(500)
    except requests.exceptions.ConnectionError:
        print ('Error Connecting')
        abort(500)
    except requests.exceptions.Timeout:
        print ('Timeout Error')
        abort(500)
    except requests.exceptions.RequestException:
        print ('Something Else')
        abort(500)
