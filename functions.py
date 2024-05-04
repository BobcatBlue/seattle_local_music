import pandas as pd
from ticketmaster_shows import get_shows

df = pd.read_csv("Seattle_ticketmaster_venues - Sheet1.csv")


def print_shows(body):
    for index, row in df.iterrows():
        venue, bands, date = get_shows(row["Venue Name"], row["vID"])
        body = body + venue + "\n"
        all_bands = []

        for b in bands:
            if "w/" in b:
                all_bands.extend([nb.strip() for nb in b.split('w/')])
                bands = all_bands
            else:
                pass

        for x, band in enumerate(bands):
            if x:
                body = body + band + ", "
            body = body + band

        body = body + "\n" + date + 2 * "\n"

        body_list = body.split("\n")

    print(body_list)
    return body_list
