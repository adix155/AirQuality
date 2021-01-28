from data import getDataFromAPI
import ipinfo
import socket
import requests
import math as m


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

def distance():
    places_list = getDataFromAPI.getStationData()
    roznicalat = ()
    roznicalon = ()
    for i in range(len(places_list)):
            roznicalat = lat[i] - float(yourLocation()[0:7]) 
            roznicalon = lon[i] - float(yourLocation()[8:])
    kwadratlat = roznicalat**(2)
    kosinus = m.cos((twojelat*m.pi)/180)
    stala = 40075.704/360
    odleglosc = (kwadratlat+(kosinus*roznicalon)**(2))**(1/2) * stala
    return odleglosc

class Test(object):

    def getStationLocation():
        places_list = getDataFromAPI.getStationData()
        for i in places_list:
            station_lat = i.lat
            station_lon = i.lon
            print(station_lat)
            print(station_lon)
        return station_lat, station_lon

distance()
#Test.getStationLocation()
#yourLocation()
    


