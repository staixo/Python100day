#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import pandas as pd
import data_manager
import flight_search
import notification_manager


dataManager = data_manager.DataManager()
existing = pd.DataFrame(dataManager.get_destination_data())
flightSearch = flight_search.FlightSearch()
#dataManager.fill_destination_codes()
print(flightSearch.search_flights("LHR"))




# Get locations