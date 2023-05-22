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
    'C:/Users/henri.peters/Downloads/test-python-214212-e4c954e48287.json', scope)  # Mettez ici le chemin vers votre fichier JSON

gc = gspread.authorize(credentials)

# Ouvrez la feuille de calcul en utilisant l'URL
spreadsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1jBk30J1hQxytNk2_jy34i77XXHFPYHXhfx98VbD49X8/edit#gid=0')
sheet = spreadsheet.sheet1
existing = gd.get_as_dataframe(sheet)


APPLICATION_ID = "94404dd4"
API_KEY = open("Python100day/Intermediate/nutrionix/data.db", "r").read()
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id":APPLICATION_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id":"0"
}

query = input("What did you do today ?")

params = {
 "query":query,
 "gender":"male",
 "weight_kg":72.5,
 "height_cm":182.64,
 "age":27
}
Today_day = datetime.today().strftime("%d/%m/%Y")
now_hour = datetime.today().strftime("%H:%M:%S")


response = requests.post(url=NUTRITIONIX_ENDPOINT, json=params, headers=headers)
print(response.status_code)
data = response.json()
print(data)
data = pd.DataFrame(data["exercises"], columns=["name", "duration_min", "nf_calories"])

existing = pd.DataFrame(existing)
existing = existing[['Exercise', 'Duration', 'Calories', 'Date', 'Time']].dropna()

data["Date"] = Today_day
data["Time"] = now_hour
print(data)
data = data.rename(columns={'duration_min': 'Duration', 'nf_calories': 'Calories', 'name': 'Exercise'})


print(data)

print(existing)

updated = pd.concat([existing, data], ignore_index=True)
print(updated)
gd.set_with_dataframe(sheet, updated)