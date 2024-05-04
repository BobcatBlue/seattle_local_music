import requests
import os
import json


API_KEY = os.getenv("ticketmaster_api_1")


def get_shows(venue_name, venueId):
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?venueId={venueId}" \
          f"&apikey={API_KEY}"

    response = requests.get(url)
    show_data = response.json()

    venue = venue_name

    try:
        band = show_data["_embedded"]["events"][0]["name"].split(", ")
        date = show_data["_embedded"]["events"][0]["dates"]["start"]["localDate"]
        return venue, band, date

    except KeyError:
        venue = venue + "\n" + " (Info unavailable through TicketMaster & TicketWeb)"
        band = ""
        date = ""
        return venue, band, date

