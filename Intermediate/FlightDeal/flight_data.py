import pandas as pd
import requests


# Connecting with kiwi

class FlightData:
    def __init__(self):
        self.KIWI_ENDPOINT = "https://tequila-api.kiwi.com"
        self.GET_LOCATIONS_ENDPOINT = f"{self.KIWI_ENDPOINT}/locations/query"
        self.KIWI_API_KEY = open("Python100day/Intermediate/FlightDeal/kiwi_api.db", "r").read()
        self.header = {"apikey": self.KIWI_API_KEY}

    def get_destination_code(self,city):
        paramskiwi = {
            "term": city,
            "location_types": "city"
            }
        response = requests.get(url=self.GET_LOCATIONS_ENDPOINT, params=paramskiwi, headers=self.header,verify=False)
        data = response.json()
        df = pd.DataFrame(data["locations"])
        return df["code"][0]
    
    def getairportcode(self,city):
        paramskiwi = {
            "term": city,
            "location_types": "airport"
            }
        response = requests.get(url=self.GET_LOCATIONS_ENDPOINT, params=paramskiwi, headers=self.header,verify=False)
        data = response.json()
        df = pd.DataFrame(data["locations"])
        return df["code"][0]
        