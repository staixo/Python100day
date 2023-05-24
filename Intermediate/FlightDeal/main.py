#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import pandas as pd
import data_manager
import flight_search
import notification_manager


dataManager = data_manager.DataManager()
existing = pd.DataFrame(dataManager.get_destination_data()).dropna()
print(dataManager.get_users())
flightSearch = flight_search.FlightSearch()
#dataManager.fill_destination_codes()



print(existing)
for index, row in existing.iterrows():
    print(row["IATA Code"])
    if row["IATA Code"] != "nan":
        df = flightSearch.search_flights(row["IATA Code"])
        if int(row["Lowest Price"]) >= int(df["price"].min()):
            print("New Lowest Price")
            print(df["price"].min())
dataManager.add_user()

