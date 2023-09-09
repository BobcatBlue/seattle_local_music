import requests
import os
import json


API_KEY = os.getenv("ticketmaster_api_1")

def get_shows(venueId):
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?venueId={venueId}&apikey={API_KEY}"
    response = requests.get(url)
    show_data = response.json()

    name = show_data["_embedded"]["events"][0]["name"]
    date = show_data["_embedded"]["events"][0]["dates"]["start"]["localDate"]

    show_info = [name, date]

    return(show_info)