
from data import getDataFromAPI
import ipinfo
import socket
import requests

def yourLocation():
    try:
        f = requests.request('GET', 'http://myip.dnsomatic.com')
        ip = f.text
        access_token = '0cd3132a1d7552'
        handler = ipinfo.getHandler(access_token)
        details = handler.getDetails(ip)
        print(details.loc[0:7])
        print(details.loc[8:])
        return details.loc
    except:
        print("Serwer przeciążony")

def getStationLocation(self):
    places_list = getDataFromAPI.getStationData(self)
    station_lat=()
    station_lon=()
    for i in places_list:
        station_lat +=  i.lat,
        station_lon += i.lon,
    print(station_lat)
    print(station_lon)


def testowanie():
    lista = getStationLocation()
    for i in lista:
        print(i.station_lat)
        print(i.station_lon)
#def stationDistance():

    
#yourLocation()
#getStationLocation()

    


