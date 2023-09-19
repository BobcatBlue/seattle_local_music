from ticketmaster_shows import get_shows
import pandas as pd


df = pd.read_csv("Seattle_ticketmaster_venues - Sheet1.csv")

body = ""

for index, row in df.iterrows():
    venue, bands, date = get_shows(row["Venue Name"], row["vID"])

    body = body + venue + "\n"

    for x, band in enumerate(bands):
        if x:
            body = body + band + ", "
        body = body + band

    body = body + "\n" + date + 2*"\n"

    #  print(f"{venue}, {band}, {date}")

print(body)