import json
import requests

class Station(object):
    def __init__(self, id, name, lat, lon, city):
        self.id = id
        self.name = name
        self.lat = lat
        self.lon = lon
        self.city = city


class getDataFromAPI(object):
    def __init__(self):
        self.placesList = []

    def placesList_get(self):
        return self.placesList

    def getStationData(self):
        url = "http://api.gios.gov.pl/pjp-api/rest/station/findAll"
        response = requests.get(url)
        data = response.text
        jsonData = json.loads(data)
        for i in range(len(jsonData)):
            id = jsonData[i]['id']
            name = jsonData[i]['stationName']
            lat = jsonData[i]['gegrLat']
            lon = jsonData[i]['gegrLon']
            city = jsonData[i]['city']['commune']['communeName']
            place = Station(id, name, lat, lon, city)
            self.placesList.append(place)


# def main():
#     o = getDataFromAPI()
#     o.getStationData()
#     print(o.placesList_get()[0])
#
# main()