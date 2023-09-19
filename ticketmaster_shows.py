import requests
import os
import json


API_KEY = os.getenv("ticketmaster_api_1")


def get_shows(venue_name, venueId):
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?venueId={venueId}" \
          f"&apikey={API_KEY}"
    print(url)
    response = requests.get(url)
    show_data = response.json()

    venue_name = ["venues", venue_name]
    band = ["bands", show_data["_embedded"]["events"][0]["name"].split(", ")]
    date = ["dates", show_data["_embedded"]["events"][0]["dates"]["start"]["localDate"]]

    info = [venue_name, band, date]

    return info

