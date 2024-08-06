import requests
import os
import json
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime


API_KEY = os.getenv("ticketmaster_api_1")


def get_shows(venue_name, venueId):
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?venueId={venueId}" \
          f"&apikey={API_KEY}"

    response = requests.get(url)
    show_data = response.json()
    try:
        all_events = show_data.get('_embedded').get('events')
    except Exception:
        band = "No info"
        date = "No info"
        return venue_name, band, date

    #Find the next show/earliest date in the list
    list_length = len(all_events)
    date_list = []
    counter = 0
    while counter < list_length:
        date = show_data.get('_embedded')['events'][counter].get('dates').get('start').get('localDate')
        date = datetime.strptime(date, "%Y-%m-%d")
        counter += 1
        date_list.append(date)
    earliest = min(date_list)
    earliest_index = date_list.index(earliest)


    try:
        show_events: list = show_data.get('_embedded').get('events')
        next_show = show_events[earliest_index]
        return venue_name, \
            next_show.get('name'), next_show.get('dates').get('start').get('localDate')

        """band_count = len(next_show.get('_embedded').get('attractions'))
        ^^ might use this later to parse out individual band names when
        I want to add links to their music
    """

    except Exception:
        band = "No info"
        date = "No info"
        return venue_name, band, date


"""
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

print(get_shows("Showbox Sodo", "KovZpa6Mee"))
"""
