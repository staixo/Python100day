#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import pandas as pd
from datetime import datetime
import gspread_dataframe as gd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Connecting with `gspread` here
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'Python100day/Intermediate/FlightDeal/credential.json.db', scope)  # Mettez ici le chemin vers votre fichier JSON

gc = gspread.authorize(credentials)

# Ouvrez la feuille de calcul en utilisant l'URL



GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/1YMK-kYDYwuiGZoawQy7zyDjEIU9u8oggCV4H2M9j7os/edit#gid=0"

spreadsheet = gc.open_by_url(GOOGLE_SHEET_URL)
sheet = spreadsheet.sheet1
existing = gd.get_as_dataframe(sheet)
existing = existing[["City", "Lowest Price"]].dropna()
print(existing)


