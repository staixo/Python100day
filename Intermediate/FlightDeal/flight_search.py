import requests
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta


from flight_data import FlightData
class FlightSearch(FlightData):
    def __init__(self):
        super().__init__()
        self.today = date.today()
        self.today = self.today.strftime("%Y-%m-%d")
        self.six_month = (date.today() + relativedelta(months=6)).strftime("%Y-%m-%d")
        self.params = {
            "fly_from":"CDG",
            "date_from":self.today,
            "date_to": self.six_month,
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 14,
            "flight_type": "round",
            "curr": "EUR"
        }
        
        self.GET_FLIGHTS_ENDPOINT = f"{self.KIWI_ENDPOINT}/v2/search"
        
    def search_flights(self,city_code):
        self.params["fly_to"] = city_code
        response = requests.get(url=self.GET_FLIGHTS_ENDPOINT, params=self.params,headers=self.header,verify=False)
        try:
            data = response.json()
            df = pd.DataFrame(data["data"])
            return df
        except IndexError:
            print(f"No flights found for {city_code}.")
            return None

    