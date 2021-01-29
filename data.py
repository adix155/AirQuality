import json
import requests

"""
klasa zawierająca parametry stacji (punktu pomiarowego):
    - id
    - nazwa
    - szerokość geograficzna
    - długość geograficzna
    - miejscowość
"""


class Station(object):
    def __init__(self, id, name, lat, lon, city):
        self.id = id
        self.name = name
        self.lat = lat
        self.lon = lon
        self.city = city


"""
klasa zawierająca właściwości danej stacji (wszystko ściągne jest z API):
- stationId - id stacji
- indexMain - dwuelementowa lista: 
    - żródłowa data 
    - tekstowa ocena ogólnego stanu powietrza w danej stacji
- pozostałe właściwości:
    - jeśli dana stacja nie mierzy danej właściwości - jednoelementowa lista zawierająca zero (print wyrzuci [0])
    - jeśli dana stacja mierzy daną właściwość - czteroelementowa lista: (print zwróci np. [6065, '2021-01-18 22:00:00', 51.9736, 'Dobry'])
        - id właściwości pomiarowej (tylko do wywołania API)
        - źródłowa data
        - wartość pomiaru (w µg/m3) (często zwraca None)
        - tekstowa ocena danej właściwości powietrza
"""


class StationProperties(object):
    def __init__(self, stationId, indexMain, indexSO2, indexNO2, indexPM10, indexPM25, indexCO, indexC6H6, indexO3):
        self.stationId = stationId
        self.indexMain = indexMain
        self.indexSO2 = indexSO2
        self.indexNO2 = indexNO2
        self.indexPM10 = indexPM10
        self.indexPM25 = indexPM25
        self.indexCO = indexCO
        self.indexC6H6 = indexC6H6
        self.indexO3 = indexO3


"""
klasa z metodami służącymi do pobierania danych z API
"""


class getDataFromAPI(object):
    """
    metoda zwracająca listę obiektów typu Station
    """

    @staticmethod
    def getStationData():
        url = "http://api.gios.gov.pl/pjp-api/rest/station/findAll"
        response = requests.get(url)
        data = response.text
        jsonData = json.loads(data)
        placesList = []
        for i in range(len(jsonData)):
            id = jsonData[i]['id']
            name = jsonData[i]['stationName']
            lat = jsonData[i]['gegrLat']
            lon = jsonData[i]['gegrLon']
            city = jsonData[i]['city']['commune']['communeName']
            place = Station(id, name, lat, lon, city)
            placesList.append(place)

            # usuwanie błędnej stacji z API
            if id == 734:
                del placesList[len(placesList) - 1]
        placesList.sort(key=lambda x: x.name)
        return placesList

    """
    metoda zwracająca obiekt typu StationProperties
        argument id: id danej stacji pomiarowej
    """

    @staticmethod
    def getStationProperties(id):
        url = 'http://api.gios.gov.pl/pjp-api/rest/station/sensors/' + str(id)
        response = requests.get(url)
        data = response.text
        jsonData = json.loads(data)

        stationId = id

        url2 = 'http://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/' + str(id)
        response2 = requests.get(url2)
        data2 = response2.text
        jsonData2 = json.loads(data2)

        indexMain = [jsonData2['stSourceDataDate'], jsonData2['stIndexLevel']['indexLevelName']]
        indexSO2 = [0]
        indexNO2 = [0]
        indexPM10 = [0]
        indexPM25 = [0]
        indexCO = [0]
        indexC6H6 = [0]
        indexO3 = [0]

        for i in range(len(jsonData)):
            if jsonData[i]['param']['idParam'] == 1:
                indexSO2.clear()
                indexSO2.append(jsonData[i]['id'])
            if jsonData[i]['param']['idParam'] == 6:
                indexNO2.clear()
                indexNO2.append(jsonData[i]['id'])
            if jsonData[i]['param']['idParam'] == 3:
                indexPM10.clear()
                indexPM10.append(jsonData[i]['id'])
            if jsonData[i]['param']['idParam'] == 69:
                indexPM25.clear()
                indexPM25.append(jsonData[i]['id'])
            if jsonData[i]['param']['idParam'] == 8:
                indexCO.clear()
                indexCO.append(jsonData[i]['id'])
            if jsonData[i]['param']['idParam'] == 10:
                indexC6H6.clear()
                indexC6H6.append(jsonData[i]['id'])
            if jsonData[i]['param']['idParam'] == 5:
                indexO3.clear()
                indexO3.append(jsonData[i]['id'])

        indexesList = [indexSO2[0], indexNO2[0], indexPM10[0], indexPM25[0], indexCO[0], indexC6H6[0], indexO3[0]]

        for i in range(len(indexesList)):
            if indexesList[i] != 0:
                url = 'http://api.gios.gov.pl/pjp-api/rest/data/getData/' + str(indexesList[i])
                response = requests.get(url)
                data = response.text
                jsonData = json.loads(data)
                date = 0
                value = 0
                for j in range(len(jsonData['values'])):
                    if jsonData['values'][j]['value'] != "null":
                        date = jsonData['values'][j]['date']
                        value = jsonData['values'][j]['value']
                        if value == None:
                            value = "?"
                        break
                if i == 0:
                    indexSO2.append(date)
                    indexSO2.append(value)
                    try:
                        indexSO2.append(jsonData2['so2IndexLevel']['indexLevelName'])
                    except TypeError:
                        indexSO2.append("?")
                if i == 1:
                    indexNO2.append(date)
                    indexNO2.append(value)
                    try:
                        indexNO2.append(jsonData2['no2IndexLevel']['indexLevelName'])
                    except TypeError:
                        indexNO2.append("?")
                if i == 2:
                    indexPM10.append(date)
                    indexPM10.append(value)
                    try:
                        indexPM10.append(jsonData2['pm10IndexLevel']['indexLevelName'])
                    except TypeError:
                        indexPM10.append("?")
                if i == 3:
                    indexPM25.append(date)
                    indexPM25.append(value)
                    try:
                        indexPM25.append(jsonData2['pm25IndexLevel']['indexLevelName'])
                    except TypeError:
                        indexPM25.append("?")
                if i == 4:
                    indexCO.append(date)
                    try:
                        indexCO.append(value/1000)
                    except TypeError:
                        indexCO.append('None')
                    try:
                        indexCO.append(jsonData2['coIndexLevel']['indexLevelName'])
                    except TypeError:
                        indexCO.append("?")

                if i == 5:
                    indexC6H6.append(date)
                    indexC6H6.append(value)
                    try:
                        indexC6H6.append(jsonData2['c6h6IndexLevel']['indexLevelName'])
                    except TypeError:
                        indexC6H6.append("?")
                if i == 6:
                    indexO3.append(date)
                    indexO3.append(value)
                    try:
                        indexO3.append(jsonData2['o3IndexLevel']['indexLevelName'])
                    except TypeError:
                        indexO3.append("?")

        stationProperties = StationProperties(stationId, indexMain, indexSO2, indexNO2, indexPM10, indexPM25, indexCO,
                                              indexC6H6,
                                              indexO3)
        return stationProperties


