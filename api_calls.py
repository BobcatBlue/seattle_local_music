import requests
import os
import json


API_KEY = os.getenv("ticketmaster_api_1")

# eu = Events URL
eu_crocodile = f"https://app.ticketmaster.com/discovery/v2/events.json?venueId=KovZpZA1vFtA&apikey={API_KEY}"


response = requests.get(eu_crocodile)
data = response.json()

print(data)

event_names = data["embedded"]["events"]["name"][0]
print(event_names)