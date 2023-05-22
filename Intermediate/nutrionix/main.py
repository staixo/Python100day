import requests
import pandas as pd

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

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=params, headers=headers)
print(response.status_code)
data = pd.dataframe(response.json())
print(data)