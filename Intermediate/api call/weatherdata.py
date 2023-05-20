import requests
import json
from twilio.rest import Client
import os



url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"


param= {
    "lat" : "0",
    "lon" : "0",
    "API_key" : "24bdf71cb44afbee00aceb388886dc09"
    }
try:
    response = requests.get(url,params=param)
    response.raise_for_status()
    data = response.json()
    print(data)
except:
    print("error")

messagebody = "Oui"
+15093003656

account_sid = 'ACabc7e86ae1c22592eecb70a7392c09f9'
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body=messagebody,
                              from_='whatsapp:+',
                              to='whatsapp:+'
                          )

print(message.sid)

