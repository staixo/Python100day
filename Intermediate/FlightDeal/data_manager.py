import pandas as pd
import gspread_dataframe as gd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import flight_data
flightdata = flight_data.FlightData()



GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/1d-tikxLqPyjrxZKNMVz5yii2P6--myHsG6_l-2oqMVg/edit?usp=sharing"



class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'Python100day/Intermediate/FlightDeal/credential.json.db', self.scope)
        self.data = None
        self.cleandata = None
        self.gc = gspread.authorize(self.credentials)
        self.spreadsheet = self.gc.open_by_url(GOOGLE_SHEET_URL)
        self.sheet = self.spreadsheet.sheet1
        
    def get_destination_data(self):

        self.data = gd.get_as_dataframe(self.sheet)
        self.cleandata = self.data[["City", "IATA Code","Lowest Price"]]
        #self.cleandata["Lowest Price"] = self.cleandata["Lowest Price"].astype(int)
        self.cleandata = pd.DataFrame(self.cleandata)
        self.cleandata = self.cleandata.drop_duplicates()
        self.cleandata =self.cleandata.reset_index(drop=True)
        return self.cleandata
    
    def fill_destination_codes(self):
        self.cleandata = self.get_destination_data()
        for city in self.cleandata["City"]:
            if city != "nan":
                self.cleandata.loc[self.cleandata["City"] == city, "IATA Code"] = flightdata.get_destination_code(city)
            else:
                break
        print(self.cleandata)
        self.gc = gspread.authorize(self.credentials)
        self.spreadsheet = self.gc.open_by_url(GOOGLE_SHEET_URL)
        self.sheet = self.spreadsheet.sheet1
        gd.set_with_dataframe(self.sheet, self.cleandata)