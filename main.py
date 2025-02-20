from io import BytesIO
import requests
from PIL import Image


class Map:
    def __init__(self, loc, delta):
        """
        :param loc: показ карты по названию или координатам
        :param delta: масштаб
        """
        self.loc = loc
        self.delta = delta
        self.map = None
        self.json_response = {}
        self.object = {}
        self.coords = ""
        self.geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    def update_map(self):
        geocoder_params = {
            "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
            "geocode": self.loc,
            "format": "json"}
        response = requests.get(self.geocoder_api_server, params=geocoder_params)
        if not response:
            pass

        self.json_response = response.json()
        self.object = self.json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        self.coords = self.object["Point"]["pos"]

        toponym = self.object
        toponym_coodrinates = toponym["Point"]["pos"]
        toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

        apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"

        map_params = {
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "spn": ",".join([self.delta, self.delta]),
            "apikey": apikey,

        }

        map_api_server = "https://static-maps.yandex.ru/v1"
        response = requests.get(map_api_server, params=map_params)
        im = BytesIO(response.content)
        self.map = im
        return self.map.getvalue()

    def show_map(self):
        self.update_map()
        op_im = Image.open(self.map)
        op_im.show()

    def change_delta(self, value, auto_update=False):
        self.delta = value
        if auto_update:
            self.update_map()

    def change_location(self, location, auto_update=False):
        self.loc = location
        if auto_update:
            self.update_map()



