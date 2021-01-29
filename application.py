from data import getDataFromAPI
import requests
import math as m
import json

try:
    url = "https://geolocation-db.com/json"
    response = requests.get(url)
    data = response.text
    jsonData = json.loads(data)
    lat = jsonData['latitude']
    lon = jsonData['longitude']
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
        kwadratlat = roznicalat ** (2)
        kosinus = m.cos((lat * m.pi) / 180)
        stala = 40075.704 / 360
        odleglosc = (kwadratlat + (kosinus * roznicalon) ** (2)) ** (1 / 2) * stala
        distances_list.append(odleglosc)
    return distances_list


def theShortest():
    lista = distance()
    shortest = lista[0]
    index = 0
    for i in range(len(lista) - 1):
        if shortest > lista[i]:
            shortest = lista[i]
            index = i
    return index

