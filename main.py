from ticketmaster_shows import get_shows
import pandas as pd


df = pd.read_csv("Seattle_ticketmaster_venues - Sheet1.csv")

venue_ids = []

# Create a dictionary in which all of the information will be stored, sorted by category
shows = {
    "venues": [],
    "bands": [],
    "dates": [],
    # "image links": [],
    # "show links": [],
}

venues = [row["Venue Name"] for index, row in df.iterrows()]
print(venues)  # this is a checker

# Fill the dictionary with info
for index, row in df.iterrows():
    show_info = get_shows(row["Venue Name"], row["vID"])
    for key, value in show_info:
        shows[key].append(value)


print(shows)

# for venue, ids in show_ids:


print(show_info)  # this is a checker

