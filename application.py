
"""from data import getDataFromAPI
import ipinfo
import socket
import requests

class AppBackground:
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

    def getStationLocation():
        places_list = getDataFromAPI.getStationData()
        station_lat=()
        station_lon=()
        for i in places_list:
            station_lat +=  i.lat,
            station_lon += i.lon,
        return station_lat,station_lon


def testowanie():
    lista = AppBackground.getStationLocation()
    for i in lista:
        print(i.station_lat,i.station_lon)

#def stationDistance():
#yourLocation()
#getStationLocation()
"""

from data import getDataFromAPI
import ipinfo
import socket
import requests
import math as m



try:
    f = requests.request('GET', 'http://myip.dnsomatic.com')
    ip = f.text
    access_token = '0cd3132a1d7552'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip)
    lat = float(details.loc[0:7])
    lon = float(details.loc[8:])
except:
    print("Serwer przeciążony")

def distance():
    distances_list = []
    places_list = getDataFromAPI.getStationData()
    roznicalat = ()
    roznicalon = ()
    odleglosc = ()
    for i in range(len(places_list)):
            roznicalat = float(places_list[i].lat) - lat 
            roznicalon = float(places_list[i].lon) - lon
            kwadratlat = roznicalat**(2)
            kosinus = m.cos((lat*m.pi)/180)
            stala = 40075.704/360
            odleglosc = (kwadratlat+(kosinus*roznicalon)**(2))**(1/2) * stala
            distances_list.append(odleglosc)
    return distances_list

def theShortest():
    lista = distance()
    shortest = lista[0]
    index = 0
    for i in range(len(lista)-1):
        if shortest>lista[i]:
           shortest = lista[i]
           index = i
    return index 



class Test(object):

    def getStationLocation():
        places_list = getDataFromAPI.getStationData()
        for i in places_list:
            station_lat = i.lat
            station_lon = i.lon
            print(station_lat)
            print(station_lon)
        return station_lat, station_lon

#theShortest()
#Test.getStationLocation()
#yourLocation()
    


